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
//             KNOT :61   62
//             CHAR : .    -
                     '9', '0'};

int ipow(int base, int exponent) {
	int result = 1;
	for (int i = 0; i < exponent; i++) {
		result *= base;
	} 
	return result;
}

int level_index(int depth) {
	// TODO refactor ipow() to here
}

int get_index(int parent_block_index, int depth, char symbol) {
	int index  = 0;
	int offset = 0;

	for (int i = 0; i < depth; i++) {
		index += ipow(2, i); 
	}
	offset = (symbol == '-')
	       ? 2*parent_block_index-1
	       : 2*parent_block_index-2;

	return index+offset;
}

char morse_to_char(char* morse) {
	int parent_block_index = 0;
	int depth              = 0;
	char result          = '-'; 
	while(*morse != '\0') {

		printf("%c\n", result);
		morse++;
	}

	return tree[0];
}

int main() {
	char result = morse_to_char("..--");
	printf("Expected K, got: %c\n", result);

	result = get_char_from_block(3, 3, '-');
	printf("Expected M, got: %c\n", result);

	return 0;
}
