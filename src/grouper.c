#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <stdarg.h>

#define SCRAMBLE_ITERATIONS 1000

FILE* outputFile;
const char* outputPath = "./groups.txt";

struct student {
	char* name;
	char* email;	
};

void cprintf(FILE* file, const char* format, ...) {
	va_list params;
	
	va_start(params, format);
	vprintf(format, params);
	va_end(params);

	va_start(params, format);
	vfprintf(file, format, params);
	va_end(params);

}

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

void loadStudents(struct student* students, char* filePath) {
	/*
	 * Loads the list of participants from a file.
	 *
	 * :param students: The content of the file will be writen to this.
	 * :param filePath: The file that is to be read.
	 *
	 * :returns: void
	 * */
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
	/*
	 *  Randomly switches the elements of an array a set amount of times.
	 *
	 *  :param students:   The array to be scrambeled.
	 *  :param buffer:     The size of the array.
	 *  :param iterations: The amount of times elements of the array are switched.
	 * */
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
	/*
	 * Creates a single group with a set amount of members.
	 *
	 * :param students:  An array of all participants of all groups.
	 * :param buffer:    The amount of participants.
	 * :param groupSize: The size of the group.
	 * :param offet:     Starting point on the array of students.
	 *
	 * :returns: void
	 * */
	for (int i = 0; i < groupSize; i++) {
		cprintf(outputFile, " - %s, Email: %s", students[offset+i].name, students[offset+i].email);

	}
	cprintf(outputFile, "\n");
}

void generateGroups(struct student students[], int buffer, int groupSize) {
	/*
	 * Creates a dynamic amount of groups based on 
	 * the amount of participants and group size.
	 * Also calculates the how many groups need to have one
	 * more member if the amount of participants can't be divided 
	 * by the group size.
	 *
	 * :param students:  An array of all participtans who are to be put into groups.
	 * :param buffer:    The amount of participants.
	 * :param groupSize: The size of each group.
	 *
	 * :returns: void
	 * */
	int overflow = buffer % groupSize;
	int groupCount = (buffer-overflow)/groupSize;
	int offset = 0;

	scrambleStudentList(students, buffer, SCRAMBLE_ITERATIONS);

	for (int i = 0; i < groupCount; i++) {
		int currentSize = (overflow > 0) ? 
			groupSize+1 : 
			groupSize;
		overflow--;
		cprintf(outputFile, "Group %i has %i members\n", i+1, currentSize);
		generateSingleGroup(students, buffer, groupSize, offset);		
		offset += currentSize;

	}

}

int main(int argc, char** argv) {
	/*
	 * This method runs the key components of the application
	 *
	 * :param argc: Amount of console parameters parsed to the 
	 *              application.
	 * :param argv: All console paramters paresed to th
	 * 		application.
	 *
	 * :returns: The exit status of the application
	 * */
	if (argc != 3) {
		printf("\033[31mInvalid parameters!\033[0m\n");
		printf("Found %i, needed 2.\n", argc);
		return -1;
	}
	
	char* filePath = argv[1];
	int groupSize = atoi(argv[2]);
	outputFile = fopen(outputPath, "w");

	int lineCount = countLines(filePath);
	printf("Students found in file: \033[32m%i\033[0m\n", lineCount);

	struct student students[lineCount];
	loadStudents(students, filePath);
	generateGroups(students, lineCount, groupSize);

	fclose(outputFile);
	return 0;
}
