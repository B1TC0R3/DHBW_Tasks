#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

struct student {
	char* name;
	char* email;	
	bool hasGroup;
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

		students[lineCounter] = (struct student){name, email, false}; 
		lineCounter++;
	}

	fclose(file);
}

void generateGroups(struct student students[], int buffer, int groupSize) {
	int overflow = buffer % groupSize;
	int groupCount = (buffer-overflow)/groupSize;
	int currentSize;

	srand(time(NULL));

	for (int i = 0; i < groupCount; i++) {
		currentSize = (overflow > 0) ? 
			groupSize+1 : 
			groupSize;
		overflow--;
		printf("Group %i has %i members\n", i, currentSize);

		for (int j = 0; j < currentSize; j++) {
			int studentIndex = rand() % buffer;
			
			while(students[studentIndex].hasGroup) {
				int direction = rand() % 2;
				studentIndex = (direction == 1) ? 
					studentIndex-1: 
					studentIndex+1;

				if (studentIndex < 0) {
					studentIndex = buffer-1;
				
				} 
				else if (studentIndex >= buffer) {
					studentIndex = 0;

				}
			}

			printf(" - %s, Email: %s", students[studentIndex].name, students[studentIndex].email);
			students[studentIndex].hasGroup = true;

		}
		puts("");

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

	for (int i = 0; i < lineCount; i++) {
		printf("%i)\tName: %s\tEmail: %s", i+1, students[i].name, students[i].email);
	}
	puts("");

	generateGroups(students, lineCount, groupSize);

	return 0;
}
