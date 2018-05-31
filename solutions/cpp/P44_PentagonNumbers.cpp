#include <cstdint>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

uint64_t penta(unsigned int n) {
    return n*(3*n-1)/2;
}

char is_penta(uint64_t m) {
    unsigned int inv = (1.0+sqrt(24*m+1)) / 6.0;
    return m == penta(inv);
}

int main(void) {
    uint64_t D_min = ~ (uint64_t) 0;
    
    vector<uint64_t> pentagonals(0);
    pentagonals.reserve(2000000);
    pentagonals.push_back(penta(1));
    unsigned int k = 2;
    do {
        uint64_t P_k = penta(k);
        pentagonals.push_back(P_k);
        for (unsigned int j = k-1; j > 0; --j) {
            uint64_t P_j = pentagonals[j-1];
            uint64_t D = P_k - P_j, S = P_k + P_j;
            if (is_penta(D) && is_penta(S)) {
                D_min = D_min > D ? D : D_min;
                break;
            }
            if (D_min < D) {
                break;
            }
        }
        if (3*k+1 > D_min) {
            break;
        }
    } while (++k);
    
    printf("Minimum difference: %llu\n", D_min);
}
