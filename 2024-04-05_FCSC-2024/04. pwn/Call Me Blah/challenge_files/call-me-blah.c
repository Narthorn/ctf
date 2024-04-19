#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int
main(void)
{
	void (*call_me)(char *);
	char blah[32];

	printf("%p\n", stdin);

	if (scanf("%zd%*c", (ssize_t *)&call_me) != 1) {
		fputs("This is not a number.\n", stderr);
		return EXIT_FAILURE;
	}

	if (fgets(blah, sizeof(blah), stdin) == NULL) {
		fputs("Read error.\n", stderr);
		return EXIT_FAILURE;
	}

    call_me(blah);

	return EXIT_SUCCESS;
}
