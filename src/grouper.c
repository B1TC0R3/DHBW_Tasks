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
	
	fclose(file);
	return lines;
}

void loadStudents(struct student* students, char* filePath, int buffer) {
	FILE* file = fopen(filePath, "r");
	char* line;
	int maxLineLength = 255;

	int lineCounter = 0;
	while(fgets(line, maxLineLength, file)) {
		students[lineCounter] = (struct student){"-NONE-", line}; 
		lineCounter++;
	}

	fclose(file);
}

int main(int argc, char** argv) {
	if (argc != 3) {
		printf("\033[31mInvalid parameters!\033[0m\n");
		printf("Found %i, needed 2.\n", argc);
		return -1;
	}
	
	char* filePath = argv[1];
	int groupSize = atoi(argv[2]);
	
	int lineCount = countLines(filePath);
	printf("Students found in file: \033[34m%i\033[0m\n", lineCount);

	return 0;
}
