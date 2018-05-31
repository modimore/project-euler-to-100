#include <stdint.h>
#include <stdio.h>
#include <math.h>

uint64_t penta(unsigned int n) {
    return n*(3*n-1)/2;
}

char is_penta(uint64_t m) {
    unsigned int inv = (1.0+sqrt(24*m+1)) / 6.0;
    return m == penta(inv);
}

int main(void) {
    uint64_t D_min = ~ (uint64_t) 0;
    
    unsigned int k = 2;
    do {
        uint64_t P_k = penta(k);
        for (unsigned int j = k-1; j > 0; --j) {
            uint64_t P_j = penta(j);
            uint64_t D = P_k - P_j, S = P_k + P_j;
            if (D_min < D) {
                break;
            }
            if (is_penta(D) && is_penta(S)) {
                D_min = D_min > D ? D : D_min;
                break;
            }
        }
        if (3*k+1 > D_min) {
            break;
        }
    } while (++k);
    
    printf("Minimum difference: %llu\n", D_min);
}
