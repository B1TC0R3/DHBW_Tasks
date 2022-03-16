#include <stdio.h>
#include <stdlib.h>

struct student{
	char* name;
	char* email;	
};

int countLines(char* filePath) {
	FILE* file = fopen(filePath, "r");
	int lines = 0;
	char ch;

	while(!feof(file)) {
		ch = fgetc(file);
		if (ch == '\n') {
			lines++;
		}
	} 

	return lines;
}

int main(int argc, char** argv) {
	if (argc != 3) {
		printf("\033[31mInvalid parameters!\033[0m\n");
		printf("Found %i, needed 2.\n", argc);
		return -1;
	}
	
	char* filePath = argv[0];
	int groupSize = atoi(argv[1]);
	
	int lineSize = countLines(filePath);
	printf("Students found in file: %i\n", lineSize);

	return 0;
}
