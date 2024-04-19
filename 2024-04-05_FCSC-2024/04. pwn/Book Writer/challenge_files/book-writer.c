#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define PG_SIZE 128

struct Book {
    void (*read)();
    void (*write)();
    char title[64];
    char *content;
    unsigned long pages;
};

struct Book * library[10] = {NULL};
int next_book = 0; // Next book

void
read_page(struct Book *bk, unsigned long page)
{
    char *p = &bk->content[(page-1)*PG_SIZE];
    printf ("\"");
    for (int i=0; i<PG_SIZE; i++)
        putchar (p[i]);
    printf("\"\n");
}

void
write_page(struct Book *bk, unsigned long page, char *str)
{
    char *p = &bk->content[(page-1)*PG_SIZE];
    strncpy (p, str, PG_SIZE-1);
}

int
pick_a_book(void)
{
    char input[64] = {0};
    int idx = -1;

    switch (next_book) {
        case 0:
            puts ("Il faut d'abord créer un livre !");
            return -1;
        case 1:
            puts ("Il y a seulement un livre");
            return 0;
        default:
            break;
    }

    while (idx < 0 || idx >= next_book) {
        printf ("Choisissez un livre: ");
        for (int i=0; i<next_book; i++)
            printf ("%d: %s  ", i, library[i]->title);
        putchar ('\n');
        fgets (input, 64, stdin);
        for (int i=0; i<64; i++) {
            if (input[i] == '\n') {
                input[i] = 0;
            }
        }
        idx = atoi (input);
    }
    return idx;
}

int
get_cmd(char *menu, char min, char max)
{
    char cmd = 0;
    while (cmd < min || cmd > max) {
        puts (menu);
        cmd = (char) getc (stdin);
        if (cmd == '\n')
            continue;
        getc (stdin); /* Enlève \n */
    }
    return cmd;
}

void
get_input(char *input, int size)
{
    fgets (input, size, stdin);
    for (int i=0; i<size; i++) {
        if (input[i] == '\n') {
            input[i] = 0;
        }
    }
    input[size-1] = 0;
}

int
main()
{
    struct Book * book;
    unsigned long page = 1;
    int current = -1;
    char cmd = 0;
    char input[64] = {0};

    while (1) {
        /* Menu */
        if (current >= 0) {
            printf ("\"%s\" est ouvert à la page %ld\n", library[current]->title, page);
            if (page < library[current]->pages) 
                cmd = get_cmd ("1: Créer un livre  2: Ouvrir un livre  3: Ecrire  4: Lire  5: Tourner la page  0: Quitter", '0', '5');
            else
                cmd = get_cmd ("1: Créer un livre  2: Ouvrir un livre  3: Ecrire  4: Lire  0: Quitter", '0', '4');
        } else {
            cmd = get_cmd ("1: Créer un livre  0: Quitter", '0', '1');
        }

        /* Exécution de la commande */
        switch (cmd) {
            case '1': /* Créer un livre */
                if (next_book > 9) {
                    puts ("10 livres maximum. La bibliothèque est pleine !");
                    break;
                }

                book = (struct Book*) malloc (sizeof(struct Book));

                puts ("Quel est le titre de ce livre ?");
                get_input (input, sizeof(input));
                strcpy(book->title, input);

                unsigned long n = 0;
                while (n<=0) {
                    printf ("Combien de pages ?\n");
                    get_input (input, sizeof(input));
                    n = strtoul (input, NULL, 10);
                }

                book->read = read_page;
                book->write = write_page;
                book->pages = n;
                book->content = (char*) malloc (n * PG_SIZE);

                library[next_book] = book;
                current = next_book++;
                page = 1;

                break;

            case '2': /* Ouvrir un livre */
                if (next_book == 0) {
                    puts ("Il n'y a pas encore de livre");
                    break;
                }
                current = pick_a_book();
                page = 1;
                break;

            case '3': /* Ecrire */
                puts ("Que voulez-vous écrire ? ");
                get_input (input, sizeof(input));
                library[current]->write(library[current], page, input);
                break;

            case '4': /* Lire */
                library[current]->read(library[current], page);
                break;

            case '5': /* Tourner la page */
                page++;
                break;

            case '0':
                puts ("bye");
                exit (0);

            default:
                break;
        }
    }

    return 0;
}
