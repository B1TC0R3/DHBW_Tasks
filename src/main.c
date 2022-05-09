// Copyright 2022 Thomas Gingele (https://github.com/Ginthom)

#include <stdio.h>

// TODO Forgot value on level 5

//            DEPTH:   0    1         2                   3                                       4
//            KNOT :   0    1    2    3    4    5    6    7    8    9   10   11    12  13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29   30
//            CHAR :        .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -
const char tree[] =  {'-', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', 'Ü', 'L', 'Ä', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', 'Ö', '-',
//             DEPTH:  5
//             KNOT : 31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59   60
//             CHAR :  .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -
	              '5', '4', '-', '3', 'E', '-', '-', '2', '&', 'E', '-', '-', '-', 'A', '-', '1', '6', '-', '/', '-', '-', '-', '(', '-', '7', '-', '-', '-', '8', '-',
//             DEPTH:
//             KNOT : 61   62
//             CHAR :  .    -
                      '9', '0'};

int ipow(int base, int exponent) {
	int result = 1;
	for (int i = 0; i < exponent; i++) {
		result *= base;
	}
	return result;
}

int depth_index(int depth) {
	int result = 0;
	for (int i = 0; i <= depth && depth >= 0; i++) {
		result += ipow(2, i);
	}
	return result;
}

char morse_to_char(char* morse) {
	int depth   = 0;
	int index   = 0;
	int block   = 0;
	int is_line = 0;
	char result = '-';

	while(*morse == '.' || *morse == '-') {
		is_line = *morse == '.' ? 0 : 1;
		block   = index - ipow(2, depth) + 1;
		index = depth_index(depth) + block*2 + is_line;  

		depth++;
		morse++;
		result = tree[index];
	}
	printf("Reached depth: %i / index: %i, block: %i\n", depth, index, block);
	return result;
}

int main() {
	char result_one = morse_to_char(".");
	printf("Expected E, Result: %c\n", result_one);

	char result_two = morse_to_char("..");
	printf("Expected I, Result: %c\n", result_two);

	char result_three = morse_to_char("-");
	printf("Expected T, Result: %c\n", result_three);

	char result_four = morse_to_char(".---");
	printf("Expected J, Result: %c\n", result_four);

	char result_five = morse_to_char("-.--");
	printf("Expected Y, Result: %c\n", result_five);

	return 0;
}
