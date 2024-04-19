#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <malloc.h>

#define MAX_FREE         6
#define MAX_FREE_SIZE 0x40

struct malloc_chunk {

  size_t mchunk_prev_size;
  size_t mchunk_size;

  struct malloc_chunk* fd;
  struct malloc_chunk* bk;

  struct malloc_chunk* fd_nextsize;
  struct malloc_chunk* bk_nextsize;
};

typedef struct malloc_chunk* mchunkptr;

#define mem2chunk(mem)       ((mchunkptr)((char*)(mem) - 2*sizeof(size_t)))
#define chunksize(p)         (chunksize_nomask (p) & ~(0x7))
#define chunksize_nomask(p)  ((p)->mchunk_size)

#define errExit(msg)        \
    do {                    \
        perror(msg);        \
        exit(EXIT_FAILURE); \
    } while(0)

void *a;

static void free_hook(void *ptr, const void *caller);
static void (*old_free_hook)(void *ptr, const void *caller);

static __attribute__ ((constructor)) void
init_hook(void)
{
    old_free_hook = __free_hook;
    __free_hook = free_hook;
}

static void
free_hook(void *ptr, const void *caller)
{
    void *result;
    size_t size = chunksize(mem2chunk(ptr));

    __free_hook = old_free_hook;

    if (size < MAX_FREE_SIZE) {
        free(ptr);
    } else {
        errExit("free error: too large");
    }

    old_free_hook = __free_hook;
    __free_hook = free_hook;

    return result;
}

void
read_string(unsigned char *buf, unsigned int size)
{
    int nbRead;

    nbRead = read(STDIN_FILENO, buf, size);
    if (nbRead < 0) {
        errExit("read error");
    }

    if (buf[nbRead - 1] == '\n') {
        buf[nbRead - 1] = 0;
    }
}

size_t
read_long()
{
    char buf[4];
    int nbRead;

    nbRead = read(STDIN_FILENO, buf, sizeof(buf));
    if (nbRead < 0) {
        errExit("read error");
    }
    return atoll(buf);
}

void
menu()
{
    printf("===== Cheapolata =====\n");
    printf(" 1. malloc\n");
    printf(" 2. free\n");
    printf(" 3. exit\n");
    printf(">>> ");
}

int
main()
{
    int ret;
    size_t size;
    unsigned int cnt_free;

    cnt_free = 0;
    while(1) {
        menu();
        switch(read_long()) {
            case 1:
                printf("Size: ");
                size = read_long();
                if (size > 0x40) {
                    fprintf(stderr, "Error: size too large.\n");
                    exit(EXIT_FAILURE);
                }

                a = malloc(size);
                if (!a) {
                    errExit("malloc error");
                }

                printf("Content: ");
                read_string(a, size);
                break;

            case 2:
                if (cnt_free < MAX_FREE) {
                    free(a);
                    cnt_free++;
                }
                break;

            case 3:
                return EXIT_SUCCESS;
        }
    }

    return EXIT_SUCCESS;
}
