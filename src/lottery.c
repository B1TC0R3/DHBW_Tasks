#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define DRAW_SIZE               6
#define NUMBERS_SIZE            49
#define SCRAMBLE_ITERATIONS     1000

void scramble(int numbers[], int buffer) {
        srand(time(NULL));

        for (int i = 0; i < SCRAMBLE_ITERATIONS; i++) {
                int first_index = rand() % buffer;
                int second_index = rand() % buffer;

                int tmp_ptr = numbers[first_index];
                numbers[first_index] = numbers[second_index];
                numbers[second_index] = tmp_ptr;

        } 

}

void draw_numbers(int result[]) {
        int numbers[NUMBERS_SIZE];

        for (int i = 0; i < NUMBERS_SIZE; i++) {
                numbers[i] = i+1;

        }

        scramble(numbers, NUMBERS_SIZE);

        for (int i = 0; i < DRAW_SIZE; i++) {
                result[i] = numbers[i];

        }

}

void bubble_sort(int list[], int buffer) {
        bool isShift = true;
        int prev_value;
        int current_value;

        while(isShift) {
                isShift = false;

                for (int i = 1; i < buffer; i++) {
                        prev_value = list[i-1];

                        if (list[i] < prev_value) {
                                list[i-1] = list[i];
                                list[i] = prev_value;

                                isShift = true;
                        }

                }

        }

}

void crprintf(int numbers[], int buffer) {
        printf("\nRESULT:\n\n\033[32m%i\t%i\t%i\n\n%i\t%i\t%i\033[0m\n\n",
              numbers[0],
              numbers[1],
              numbers[2],
              numbers[3],
              numbers[4],
              numbers[5]);
}

int main(int argc, const char** argv) {
        if (argc > 1) printf("Parameters ignored: \033[32m%i\033[0m\n", argc-1);

        int numbers[DRAW_SIZE];
        draw_numbers(numbers); 

        bubble_sort(numbers, DRAW_SIZE);

        crprintf(numbers, DRAW_SIZE);

}
