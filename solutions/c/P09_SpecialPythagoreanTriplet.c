#include <stdio.h>

unsigned int TRIPLE_SUM = 1000;

int main(void) {
    unsigned int a = 0, b = 0, c = TRIPLE_SUM / 2;
    
    unsigned int longest_side_minlength = TRIPLE_SUM / 3;
    
    while (c > longest_side_minlength) {
        for (b = 0; b < c; ++b) {
            for (a = 0; a < b; ++a) {
                if (a + b + c == TRIPLE_SUM) {
                    if (a * a + b * b ==  c * c) {
                        printf("%d, %d, %d\n", a, b, c);
                        return 0;
                    }
                    else if (a * a + b * b > c * c) {
                        a = b = c;
                    }
                }
            }
        }
        --c;
    }
}
