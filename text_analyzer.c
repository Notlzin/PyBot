// text_analyzer.c
#include <stdio.h>
#include <ctype.h>

int main() {
    int letters=0, words=0, c, in_word=0;
    while ((c = getchar()) != EOF) {
        if (isalpha(c)) letters++;
        if (isspace(c)) in_word = 0;
        else if (!in_word) {
            in_word = 1;
            words++;
        }
    }

    printf("[C Analyzer] Letters: %d, Words: %d\n", letters, words);
    return 0;
}
