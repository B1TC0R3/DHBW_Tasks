#include <stdio.h>

const char* const GREEN = "\033[32m";
const char* const RED = "\033[31m";
const char* const CYAN = "\033[36m";
const char* const NONE = "\033[0m";

struct month {
	char name[3];
	float tmax;
	float tmin;
};

void loadYear(struct month year[12]) 
{
	year[0] = (struct month){"Jan", 2.1f, -2.8f };
	year[1] = (struct month){"Feb", 3.5f, -2.4f};
	year[2] = (struct month){"Mar", 7.4f, 0.2f};
	year[3] = (struct month){"Apr", 11.7f, 3.0f};
	year[4] = (struct month){"May", 16.8f, 7.2f};
	year[5] = (struct month){"Jun", 20.0f, 10.5f};
	year[6] = (struct month){"Jul", 21.8f, 12.3f};
	year[7] = (struct month){"Aug", 21.7f, 12.2f};
	year[8] = (struct month){"Sep", 18.3f, 9.6};
	year[9] = (struct month){"Okt", 13.2f, 5.9f};
	year[10] = (struct month){"Nov", 7.0f, 1.7f};
	year[11] = (struct month){"Dez", 3.4f, -1.3f};
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
