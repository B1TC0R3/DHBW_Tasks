#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
	if (argc != 2)
		printf("\033[31mInvalid parameters!\033[0m\n");
	
	char* filePath = argv[0];
	int groupSize = atoi(argv[1]);

	return 0;
}
