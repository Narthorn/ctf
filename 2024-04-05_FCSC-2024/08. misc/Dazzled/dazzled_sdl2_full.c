#include <SDL2/SDL.h>
#include <SDL2/SDL_ttf.h>

// compile with `gcc dazzled_sdl2_full.c -O3 -lm -lSDL2 -lSDL2main -lSDL2_ttf -o dazzled_sdl2_full`

#define DEFAULT_FONT_PATH "/usr/share/fonts/TTF/OpenSans-Regular.ttf" // can pass a different path as commandline argument

typedef double         f64;
typedef signed   long  s64;
typedef unsigned long  u64;
typedef unsigned short u16;
typedef unsigned char  u8;

#define WINDOW_WIDTH  512
#define WINDOW_HEIGHT 512

#define SPOT_SAMPLES 50.0 // better leave these as floats or else
#define MIN_X -4.
#define MAX_X 5
#define MIN_Y -4.
#define MAX_Y 5

f64 x_resolution = WINDOW_WIDTH/(MAX_X - MIN_X);
f64 y_resolution = WINDOW_HEIGHT/(MAX_Y - MIN_Y);

typedef struct Vec3 { f64 x; f64 y; f64 z; } Vec3;

Vec3 add(Vec3 a, Vec3 b) { a.x += b.x; a.y += b.y; a.z += b.z; return a; }
Vec3 sub(Vec3 a, Vec3 b) { a.x -= b.x; a.y -= b.y; a.z -= b.z; return a; }
Vec3 mul(Vec3 a, f64 k)  { a.x *= k;   a.y *= k;   a.z *= k;   return a; }

f64 dot(Vec3 a, Vec3 b) { return a.x * b.x + a.y * b.y + a.z * b.z; }

typedef struct Matrix { f64 d[3][3]; } Matrix;

Vec3 matrix_mul(Matrix m, Vec3 p) {
    return (Vec3){
        m.d[0][0] * p.x + m.d[0][1] * p.y + m.d[0][2] * p.z,
        m.d[1][0] * p.x + m.d[1][1] * p.y + m.d[1][2] * p.z,
        m.d[2][0] * p.x + m.d[2][1] * p.y + m.d[2][2] * p.z,
    };
}

Matrix rotation_matrix(Vec3 axis, f64 angle) {
    angle = 2*M_PI * angle/360;
    axis = mul(axis, sin(angle / 2.0)/sqrt(dot(axis, axis)));
    f64 a = cos(angle / 2.0), b = axis.x, c = axis.y, d = axis.z;
    return (Matrix){{
        {a*a + b*b - c*c - d*d,     2 * (b*c + a*d),       2 * (b*d - a*c)   },
        {   2 * (b*c - a*d),     a*a + c*c - b*b - d*d,    2 * (c*d + a*b)   },
        {   2 * (b*d + a*c),        2 * (c*d - a*b),    a*a + d*d - b*b - c*c},
    }};
}


Vec3 beam_axis = { 0, 1, 0};
Vec3 tilt_axis = { 1, 0, 0};
Vec3 pan_axis  = { 0, 0, 1};

Vec3 rotate_projector(Vec3 beam_axis, f64 pan, f64 tilt) {
    Vec3 panned_beam_axis = matrix_mul(rotation_matrix(pan_axis, pan), beam_axis);
    Vec3 panned_tilt_axis = matrix_mul(rotation_matrix(pan_axis, pan), tilt_axis);

    return matrix_mul(rotation_matrix(panned_tilt_axis, tilt), panned_beam_axis);
}

Vec3 raycast(Vec3 beam_origin, Vec3 beam_axis, Vec3 plane_normal, f64 plane_distance) {
    return add(beam_origin, mul(beam_axis, (plane_distance - dot(beam_origin, plane_normal)) / dot(beam_axis, plane_normal)));
}

f64 lerp(f64 a, f64 b, f64 t) { return a + (b-a)*t; }

typedef Vec3 Pixels[WINDOW_HEIGHT][WINDOW_WIDTH];

typedef struct Projector {
    u8 color;
    u8 dimmer;
    u16 pan;
    u16 tilt;
} __attribute__((packed)) Projector; // packing is not strictly needed here, but it would be if you wanted to add the other projector parameters

typedef struct State {
    s64 frame;
    f64 pan;
    f64 tilt;
    f64 height;
    f64 spacing_x;
    f64 spacing_y;
    f64 spot_size;
    u8 paused;
} State;

void main(int argc, char *argv[]) {

    char *font_path = DEFAULT_FONT_PATH;
    if (argc > 1) font_path = argv[1];

    Vec3 colormap[256];
    for (int i =   0; i<  9; i++) colormap[i] = (Vec3){255,255,255}; // white
    for (int i =   9; i< 18; i++) colormap[i] = (Vec3){255,0,0};     // red
    for (int i =  18; i< 26; i++) colormap[i] = (Vec3){255,128,0};   // orange
    for (int i =  26; i< 35; i++) colormap[i] = (Vec3){0,255,200};   // cyan-green
    for (int i =  35; i< 43; i++) colormap[i] = (Vec3){0,255,0};     // green
    for (int i =  43; i< 52; i++) colormap[i] = (Vec3){128,255,128}; // light green
    for (int i =  52; i< 60; i++) colormap[i] = (Vec3){128,0,128};   // purple
    for (int i =  60; i< 69; i++) colormap[i] = (Vec3){255,107,95};  // pink
    for (int i =  69; i< 77; i++) colormap[i] = (Vec3){255,255,0};   // yellow
    for (int i =  77; i< 86; i++) colormap[i] = (Vec3){255,165,0};   // magenta
    for (int i =  86; i< 94; i++) colormap[i] = (Vec3){0,255,255};   // cyan
    for (int i =  94; i<103; i++) colormap[i] = (Vec3){128,128,128}; // CTO 190k (not really)
    for (int i = 103; i<111; i++) colormap[i] = (Vec3){165,165,165}; // CTO 240k (not really)
    for (int i = 111; i<120; i++) colormap[i] = (Vec3){64,64,64};    // CTB 7000k (not really)
    for (int i = 120; i<128; i++) colormap[i] = (Vec3){0,0,255};     // blue

    TTF_Init();
    TTF_Font* font = TTF_OpenFont(font_path, 16);
    if (!font) { printf("font \"%s\" not found or couldn't be loaded, pass another one as argument\n", font_path); return; }

    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("dazzled", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED || SDL_RENDERER_PRESENTVSYNC);
    SDL_GL_SetSwapInterval(1);

#if 0 // aaah, we aint c23 yet
    Projector frame_data[] = {
    #embed "dazzled_data"
    };
    u64 n_frames = sizeof(frame_data) / 16;
#else
    FILE *data = fopen("dazzled_data", "r");
    if (!data) { printf("couldn't open dazzled_data\n"); return; }
    fseek(data, 0, SEEK_END);
    u64 size = ftell(data);
    rewind(data);

    u64 frame_size = sizeof(Projector)*16;
    u64 n_frames = size / frame_size;

    Projector *frame_data = malloc(size);
    fread(frame_data, frame_size, n_frames, data);
    fclose(data);
#endif

    // don't want that on the stack unless you want to make the stack big
    Pixels *pixels = malloc(sizeof(Pixels));

    State state = {
        .frame = 0,
        .pan = 0,
        .tilt = 135,
        .height = -2.8,
        .spacing_x = 0.57,
        .spacing_y = 0.67,
        .spot_size = 8,
        .paused = 0,
    };
    State prev_state = {-1};

    SDL_Event event;
    while (1) {

        while (SDL_PollEvent(&event)) {
            switch (event.type) {
                case SDL_QUIT: return;
                case SDL_KEYDOWN:
                    if (event.key.keysym.scancode != SDL_SCANCODE_SPACE) state.paused = 1;
                    switch(event.key.keysym.scancode) {

                        case SDL_SCANCODE_RIGHT:     state.frame += 120; break;
                        case SDL_SCANCODE_LEFT:      state.frame -= 120; break;
                        case SDL_SCANCODE_UP:        state.tilt += 1; break;
                        case SDL_SCANCODE_DOWN:      state.tilt -= 1; break;
                        case SDL_SCANCODE_PAGEUP:    state.height += 0.1; break;
                        case SDL_SCANCODE_PAGEDOWN:  state.height -= 0.1; break;
                        case SDL_SCANCODE_HOME:      state.spot_size += 0.1; break;
                        case SDL_SCANCODE_END:       state.spot_size -= 0.1; break;
                        case SDL_SCANCODE_INSERT:    state.pan += 1; break;
                        case SDL_SCANCODE_DELETE:    state.pan -= 1; break;


                        case SDL_SCANCODE_SPACE: state.paused = (1-state.paused); break;
                        case SDL_SCANCODE_R:     state.paused = 0; state.frame = 0; break;

                        case SDL_SCANCODE_ESCAPE: return;
                        case SDL_SCANCODE_A:      return;
                    }
                    break;
            }
        }


        if (memcmp(&state, &prev_state, sizeof(State)) == 0) goto done; // naughty but GCC will set padding to zero so it's fine

        state.frame = (state.frame + n_frames)%n_frames;
        state.pan   = fmod(state.pan + 540,360) - 180;
        state.tilt  = fmod(state.tilt + 540,360) - 180;

        Projector *projectors = frame_data + (state.frame * 16);
        memset(pixels, 0, sizeof(Pixels));

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
        SDL_RenderClear(renderer);

        for (int i=0; i<16; i++) {

            Projector projector = projectors[i];
            if (projector.dimmer == 0) continue;

            Vec3 pos = {state.spacing_x * (i%4), state.spacing_y * (i/4), state.height};
            f64 pan  = projector.pan/65535. * 540 + state.pan;
            f64 tilt = projector.tilt/65535. * 270 + state.tilt;

            Vec3 projector_axes[3] = {
                rotate_projector(beam_axis, pan, tilt),
                rotate_projector(tilt_axis, pan, tilt),
                rotate_projector(pan_axis, pan, tilt),
            };

            for (u64 lr = 0; lr < SPOT_SAMPLES; lr++) {
                for (u64 tb = 0; tb < SPOT_SAMPLES; tb++) {

                    f64 lr_angle = lerp(-state.spot_size/2, state.spot_size/2, lr/SPOT_SAMPLES);
                    f64 tb_angle = lerp(-state.spot_size/2, state.spot_size/2, tb/SPOT_SAMPLES);
                    if (pow(lr_angle,2) + pow(tb_angle,2) > pow(state.spot_size/2,2)) continue;

                    Vec3 p = raycast(pos, matrix_mul(rotation_matrix(projector_axes[1],tb_angle), matrix_mul(rotation_matrix(projector_axes[2],lr_angle), projector_axes[0])), (Vec3){0,0,1}, 0);

                    if (p.x < MIN_X || MAX_Y <= p.x) continue;
                    if (p.y < MIN_Y || MAX_Y <= p.y) continue;

                    u64 x = (p.x - MIN_X) * x_resolution;
                    u64 y = (p.y - MIN_Y) * y_resolution;

                    Vec3 c = add((*pixels)[y][x], colormap[projector.color]);
                    if (c.x > 255) c.x = 255;
                    if (c.y > 255) c.y = 255;
                    if (c.z > 255) c.z = 255;
                    (*pixels)[y][x] = c;

                    SDL_SetRenderDrawColor(renderer, (*pixels)[y][x].x, (*pixels)[y][x].y, (*pixels)[y][x].z, SDL_ALPHA_OPAQUE);
                    SDL_RenderDrawPoint(renderer, x, y);
                }
            }

        }

        char info[1000];
        sprintf(info, "pan: %.0f\ntilt: %.2f\nheight: %.2f\nspot size: %.2f\nspacing_x: %.2f\nspacing_y: %.2f\n", state.pan, state.tilt, state.height, state.spot_size, state.spacing_x, state.spacing_y);
        SDL_Surface* textSurface = TTF_RenderText_Blended_Wrapped(font, info, (SDL_Color){255, 255, 255, 255}, 200);
        SDL_Texture* text = SDL_CreateTextureFromSurface(renderer, textSurface);
        SDL_FreeSurface(textSurface);
        SDL_RenderCopy(renderer, text, NULL, &((SDL_Rect){ 10, 10, textSurface->w, textSurface->h }));
        SDL_DestroyTexture(text);

        done:

        SDL_RenderPresent(renderer);

        prev_state = state;

        if (!state.paused) state.frame++;
    }
}


