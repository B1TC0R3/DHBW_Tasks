#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

#define SCRAMBLE_ITERATIONS 1000

struct student {
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
	int maxLineLength = 255;
	char line[maxLineLength];

	int lineCounter = 0;
	while(fgets(line, maxLineLength, file) != NULL) {
		char* email = malloc(strlen(line));
		strcpy(email, line);

		char* currentName = strtok(line, "@");
		char* name = malloc(strlen(currentName));
		strcpy(name, currentName);

		students[lineCounter] = (struct student){name, email}; 
		lineCounter++;
	}

	fclose(file);
}

void scrambleStudentList(struct student students[], int buffer, int iterations) {
	int firstIndex; 
	int secondIndex;

	struct student tmp;

	srand(time(NULL));
	for (int i = 0; i < iterations; i++) {
		firstIndex = rand() % buffer;
		secondIndex = rand() % buffer;

		tmp = students[firstIndex];
		students[firstIndex] = students[secondIndex];
		students[secondIndex] = tmp;
	}

}

void generateSingleGroup(struct student students[], int buffer, int groupSize, int offset) {
	for (int i = 0; i < groupSize; i++) {
		printf(" - %s, Email: %s", students[offset+i].name, students[offset+i].email);

	}
	puts("");
}

void generateGroups(struct student students[], int buffer, int groupSize) {
	int overflow = buffer % groupSize;
	int groupCount = (buffer-overflow)/groupSize;
	int offset = 0;

	scrambleStudentList(students, buffer, SCRAMBLE_ITERATIONS);

	for (int i = 0; i < groupCount; i++) {
		int currentSize = (overflow > 0) ? 
			groupSize+1 : 
			groupSize;
		overflow--;
		printf("Group %i has %i members\n", i+1, currentSize);
		generateSingleGroup(students, buffer, groupSize, offset);		
		offset += currentSize;

	}

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
	printf("Students found in file: \033[32m%i\033[0m\n", lineCount);

	struct student students[lineCount];
	loadStudents(students, filePath, lineCount);
	generateGroups(students, lineCount, groupSize);

	return 0;
}
