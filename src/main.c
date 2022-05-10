#include "iterative_binary_tree.h"

int main() {
	char result = morse_to_text(".-..");
	printf("L: %c\n", result);
	result = morse_to_text("--.");
	printf("G: %c\n", result);
}
