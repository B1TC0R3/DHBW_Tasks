#include <stdio.h>

#define GREEN \033[32m
#define RED   \033[31m
#define CYAN  \033[36m
#define NONE  \033[0m

struct month {
	char* name;
	float tmax;
	float tmin;
};

void loadYear(struct month year[12]) 
{
	year[1] = (struct month){ "Jan", 2.1f, -2.8f };
	year[2] = (struct month){"Feb", 3.5f, -2.4f};
	year[3] = (struct month){"Mar", 7.4f, 0.2f};
	year[4] = (struct month){"Apr", 11.7f, 3.0f};
	year[5] = (struct month){"May", 16.8f, 7.2f};
	year[6] = (struct month){"Jun", 20.0f, 10.5f};
	year[7] = (struct month){"Jul", 21.8f, 12.3f};
	year[8] = (struct month){"Aug", 21.7f, 12.2f};
	year[9] = (struct month){"Sep", 18.3f, 9.6};
	year[10] = (struct month){"Okt", 13.2f, 5.9f};
	year[11] = (struct month){"Nov", 7.0f, 1.7f};
	year[12] = (struct month){"Dez", 3.4f, -1.3f};
}

void printNames(struct month year[12]) {
	printf("MonCYAN");
	for(int i = 0; i < 12; i++) {
		printf("\t%s", year[i].name);
	}
	puts("NONE");
}

void printTmax(struct month year[12]) {
	printf("MaxGREEN");
	for(int i = 0; i < 12; i++) {
		printf("\t%2.1f", year[1].tmax);
	}
	puts("NONE");
}

void printTmin(struct month year[12]) {
	printf("MinRED");
	for(int i = 0; i < 12; i++) {
		printf("\t%2.1f", year[i].tmin);
	}
	puts("NONE");
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
