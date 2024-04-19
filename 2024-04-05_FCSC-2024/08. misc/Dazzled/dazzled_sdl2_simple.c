#include <SDL2/SDL.h>

// compile with `gcc sdl2_dazzled_simple.c -O3 -lm -lSDL2 -lSDL2main -o sdl2_dazzled_simple`

typedef struct Vec3 { float x; float y; float z; } Vec3;

Vec3 add(Vec3 a, Vec3 b) { a.x += b.x; a.y += b.y; a.z += b.z; return a; }
Vec3 sub(Vec3 a, Vec3 b) { a.x -= b.x; a.y -= b.y; a.z -= b.z; return a; }
Vec3 mul(Vec3 a, float k) { a.x *= k;  a.y *= k;   a.z *= k;   return a; }

float dot(Vec3 a, Vec3 b) { return a.x * b.x + a.y * b.y + a.z * b.z; }

Vec3 beam_axis = { 0, 1, 0};
Vec3 tilt_axis = { 1, 0, 0};
Vec3 pan_axis  = { 0, 0, 1};

typedef struct Matrix { float d[3][3]; } Matrix;

Matrix rotation_matrix(Vec3 axis, float angle) {
    angle = angle/360 * 2*M_PI;
    axis = mul(axis, sin(angle / 2.0)/sqrt(dot(axis, axis)));
    float a = cos(angle / 2.0), b = axis.x, c = axis.y, d = axis.z;
    return (Matrix){{
        {a*a + b*b - c*c - d*d,  2 * (b*c + a*d),       2 * (b*d - a*c)      },
        {2 * (b*c - a*d),        a*a + c*c - b*b - d*d, 2 * (c*d + a*b)      },
        {2 * (b*d + a*c),        2 * (c*d - a*b),       a*a + d*d - b*b - c*c},
    }};
}

Vec3 matrix_mul(Matrix m, Vec3 p) {
    return (Vec3){
        m.d[0][0] * p.x + m.d[0][1] * p.y + m.d[0][2] * p.z,
        m.d[1][0] * p.x + m.d[1][1] * p.y + m.d[1][2] * p.z,
        m.d[2][0] * p.x + m.d[2][1] * p.y + m.d[2][2] * p.z,
    };
}

Vec3 rotate_projector(Vec3 beam_axis, float pan, float tilt) {
    Vec3 panned_beam_axis = matrix_mul(rotation_matrix(pan_axis, pan), beam_axis);
    Vec3 panned_tilt_axis = matrix_mul(rotation_matrix(pan_axis, pan), tilt_axis);

    return matrix_mul(rotation_matrix(panned_tilt_axis, tilt), panned_beam_axis);
}

Vec3 raycast_to_ground(Vec3 beam_origin, Vec3 beam_axis) {
    return add(beam_origin, mul(beam_axis, -beam_origin.z / beam_axis.z));
}

#define MIN_X -1.
#define MAX_X 3.5
#define MIN_Y -1.
#define MAX_Y 3.5

#define WINDOW_WIDTH  512
#define WINDOW_HEIGHT 512
float x_resolution = WINDOW_WIDTH/(MAX_X - MIN_X);
float y_resolution = WINDOW_HEIGHT/(MAX_Y - MIN_Y);

float spacing_x = 0.57;
float spacing_y = 0.67;
float height = -2.8;

void main() {

    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window *window = SDL_CreateWindow("dazzled", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, SDL_WINDOW_SHOWN);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED || SDL_RENDERER_PRESENTVSYNC);
    SDL_GL_SetSwapInterval(1); // force vsync

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

    typedef struct Projector {
        char color;
        char dimmer;
        unsigned short pan;
        unsigned short tilt;
    } Projector;

    FILE *data = fopen("dazzled_data", "r");
    if (!data) { printf("Couldn't open dazzled_data\n"); return; }
    fseek(data, 0, SEEK_END);
    long size = ftell(data);
    rewind(data);

    int frame_size = sizeof(Projector)*16;
    int n_frames = size / frame_size;

    Projector *frame_data = malloc(size);
    fread(frame_data, frame_size, n_frames, data);
    fclose(data);

    float tilt_offset = 0;
    float pan_offset = 0;
    char paused = 0;

    int frame = 0;
    while (1) {

        frame = frame % n_frames; // loop when we get to the end
        Projector *projectors = frame_data + (16*frame); // this is pointer arithmetic, so sizeof(Projector) is already taken into account

        SDL_Event event;
        SDL_PollEvent(&event);
        if (event.type == SDL_QUIT) return;
        if (event.type == SDL_KEYDOWN) {
            switch(event.key.keysym.sym) {
                case SDLK_DOWN:  tilt_offset -= 1;  break;
                case SDLK_UP:    tilt_offset += 1;  break;
                case SDLK_LEFT:  pan_offset -= 1;   break;
                case SDLK_RIGHT: pan_offset += 1;   break;
                case SDLK_SPACE:  paused = 1-paused; break;
                case SDLK_ESCAPE: return;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
        SDL_RenderClear(renderer);

        for (int i=0; i<16; i++) {

            Projector projector = projectors[i];
            if (projector.dimmer == 0) continue;

            Vec3 beam_origin = {spacing_x * (i%4), spacing_y * (i/4), height};
            float pan  = projector.pan/65535. * 540 + tilt_offset;
            float tilt = projector.tilt/65535. * 270 + pan_offset;

            Vec3 p = raycast_to_ground(beam_origin, rotate_projector(beam_axis, pan, tilt));

            if (p.x < MIN_X || MAX_Y <= p.x) continue;
            if (p.y < MIN_Y || MAX_Y <= p.y) continue;

            int x = (p.x - MIN_X) * x_resolution;
            int y = (p.y - MIN_Y) * y_resolution;

            Vec3 color = colormap[projector.color];
            SDL_SetRenderDrawColor(renderer, color.x, color.y, color.z, SDL_ALPHA_OPAQUE);

            for (int dx=-2; dx<3; dx++) {      // paint a few pixels around the target 
                for (int dy=-2; dy<3; dy++) {  // to make the dots thicker and easier to see
                    SDL_RenderDrawPoint(renderer, x+dx, y+dy);
                }
            }
        }

        SDL_RenderPresent(renderer);

        if (!paused) frame++;

    }
}

