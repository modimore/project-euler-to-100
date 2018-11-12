#include <iostream>
#include <utility>
#include "euler_util\PrimeCache.hpp"

std::pair<long long, unsigned int> find_best_pair(unsigned int max_coeff) {
    PrimeCache primes;
    std::pair<int, unsigned int> best(0, 0);
    unsigned int longest_run = 0;
    for (PrimeIterator p = primes.begin(); *p < max_coeff+1; ++p) {
        unsigned int b = *p;
        for (int a = - (int)max_coeff + 1; a < (int) max_coeff; ++a) {
            long long n = 0;
            long long f_n = n*n + a*n + b;
            while (primes.contains(f_n)) {
                n += 1;
                f_n = n*n + a*n + b;
            }
            if (n > longest_run) {
                best = std::pair<int, unsigned int>(a, b);
                longest_run = n;
            }
        }
    }
    return best;
}

int main(int argc, char **argv) {
    unsigned int n = 1000;
    std::pair<int, unsigned int> best_pair = find_best_pair(n);
    long long product = (long long) best_pair.first * best_pair.second;
    std::cout << "a, b: " << best_pair.first << ", " << best_pair.second << std::endl;
    std::cout << "Solution: " << product << std::endl;
    return 0;
}