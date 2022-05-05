#include <stdio.h>

//            DEPTH:   0    1         2                   3
//            KNOT :   0    1    2    3    4    5    6    7    8    9   10   11    12  13   14   15   16   17   18   19   20   21   22   23   24   25   26   27   28   29
//            CHAR :        .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -
const char tree[] =  {'-', 'E', 'T', 'I', 'A', 'N', 'M', 'S', 'U', 'R', 'W', 'D', 'K', 'G', 'O', 'H', 'V', 'F', 'Ü', 'L', 'Ä', 'P', 'J', 'B', 'X', 'C', 'Y', 'Z', 'Q', 'Ö', '-',
//             DEPTH:  4 
//             KNOT : 30   31   32   33   34   35   36   37   38   39   40   41   42   43   44   45   46   47   48   49   50   51   52   53   54   55   56   57   58   59
//             CHAR :  .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -    .    -
	              '5', '4', '-', '3', 'E', '-', '-', '2', '&', 'E', '-', '-', '-', 'A', '-', '1', '6', '-', '/', '-', '-', '-', '(', '-', '7', '-', '-', '-', '8', '-', 
//             DEPTH:
//             KNOT :60   61
//             CHAR : .    -
                     '9', '0'};

char get_char(int parent_index, int depth, char symbol) {
	int index = 0;
	int level_end_index = 0;
	for (int i = 0; i <= depth; i++) {
		level_end_index += 2^i; 
	}

	switch (symbol) {
		case '.':
			break;
		case '-':
			break;
	}
}

void print_char_from_morse(char* morse_code) {
	
}

int main() {
	char result = get_char(1, 1, '.');
	printf("Got char: %c\n", result);
	return 0;
}
