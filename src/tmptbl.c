#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char* const GREEN = "\033[32m";
const char* const RED = "\033[31m";
const char* const CYAN = "\033[36m";
const char* const NONE = "\033[0m";

struct month {
	char* name;
	float tmax;
	float tmin;
};

void loadYear(struct month year[12]) 
{
	FILE* file = fopen("tmp.csv", "r");
	int buffer = 32;
	char line[buffer];
	const char* delimiter = ",";

	if(file == NULL){
		printf("%sFailed to open file!%s\n", RED, NONE);
		return;
	}
	
	int counter = 0;
	while(fgets(line, buffer, file)) {
		char* ldup = strdup(line);

		char* name = strsep(&ldup, delimiter);
		float tmax = atof(strsep(&ldup, delimiter));
		float tmin = atof(ldup);

		year[counter] = (struct month){name, tmax, tmin};
		counter++;
	}

	fclose(file);
}

void printNames(struct month year[12]) {
	printf("Mon%s", CYAN);
	for(int i = 0; i < 12; i++) {
		printf("\t%c%c%c", year[i].name[0], year[i].name[1], year[i].name[2]);
	}
	printf("%s\n", NONE);
}

void printTmax(struct month year[12]) {
	printf("Max%s", GREEN);
	for(int i = 0; i < 12; i++) {
		printf("\t%2.1f", year[i].tmax);
	}
	printf("%s\n", NONE);
}

void printTmin(struct month year[12]) {
	printf("Min%s", RED);
	for(int i = 0; i < 12; i++) {
		printf("\t%2.1f", year[i].tmin);
	}
	printf("%s\n", NONE);
}

void printYear(struct month year[12]) 
{
	printNames(year);
	printTmax(year);
	printTmin(year);
}

int main() {
	struct month year[12];
	loadYear(year);
	printYear(year);
}
