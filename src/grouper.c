#include <stdio.h>

int main(int argc, char** argv) {
	if (argc != 2)
		printf("\033[31mInvalid parameters!");
	return 0;
}
