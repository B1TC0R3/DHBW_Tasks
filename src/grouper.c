#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <stdarg.h>
#include <unistd.h>

#define SCRAMBLE_ITERATIONS 1000

FILE* outputFile;

struct student {
	/*
	 * Represents a single student.
	 * */
	char* name;
	char* email;	
};

void cprintf(FILE* file, const char* format, ...) {
	/*
	 * Prints to the console and a file at the same time.
	 *
	 * :param file:   The file that is to be written to.
	 * :param format: The format that the remaining parameters are to be printed in.
	 * :param ...:    The values that are to be inserted into the format.
	 *
	 * :returns: void
	 * */
	va_list params;
	
	va_start(params, format);
	vprintf(format, params);
	va_end(params);

	va_start(params, format);
	vfprintf(file, format, params);
	va_end(params);

}

int countLines(char* filePath) {
	/*
	 * Counts the lines of a file.
	 *
	 * :param filePath: The path to the file whichs lines will be counted.
	 *
	 * :returns: int | The amount of lines in the file.
	 * */
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

void printHelp() {
	puts("Grouper (1)\n");
	printf("\033[32mNAME\033[0m\n\tgrouper - create random groups from a list of email addresses\n\n"); 
	printf("\033[32mSYNPOSIS\033[0m\n\t\033[32m./grouper\033[0m [\033[36mOPTION\033[0m]...\n\n");
	printf("\033[32mDESCRIPTION\033[0m\n\tCreate a group from a list of emails read in from a file\n");
	printf("\tWill output into a file and to the console at the same time\n\n");
	printf("\t\033[32m-i\033[0m\n\t\tPath to the input file\n\t\tThis is a required parameter\n\n");
	printf("\t\033[32m-s\033[0m\n\t\tSets the group size\n\t\tDefaults to \033[32m5\033[0m\n\n");
	printf("\t\033[32m-o\033[0m\n\t\tSets the output file\n\t\tThis is a required parameter\n\n");
	printf("\t\033[32m-h\033[0m\n\t\tPrint help about the command\n\n");
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
	int option = -1;
	int groupSize = 5;
	char* inputPath = malloc(255);
	char* outputPath = malloc(255);

	while ((option = getopt(argc, argv, "i:s:o:h")) != -1) {
		switch(option) {
			case 'i':
				strcpy(inputPath, optarg);		
				break;
			case 's':
				groupSize = atoi(optarg);
				break;
			case 'o':
				strcpy(outputPath, optarg);
				break;
			case 'h':
			case '?':	
			default:
				printHelp();
				return -1;
				break;
		}
			
	}
	
	outputFile = fopen(outputPath, "w");

	int lineCount = countLines(inputPath);
	printf("Students found in file: \033[32m%i\033[0m\n", lineCount);

	struct student students[lineCount];
	loadStudents(students, inputPath);
	generateGroups(students, lineCount, groupSize);

	fclose(outputFile);
	free(inputPath);
	free(outputPath);
	return 0;

}
