#include <cstring>
#include <iostream>
#include "euler_util/primes.hpp"

unsigned long long largest_prime_factor(unsigned long long n) {
    using primes::primes;
    unsigned long long best_prime;
    for (auto p = primes.begin(); *p <= n; ++p) {
        while (n % *p == 0) {
            n = n / *p;
            best_prime = *p;
        }
    }
    
    return best_prime;
}

int main(int argc, char **argv) {
    unsigned long long n = argc == 1 ? 600851475143 : atoll(argv[1]);
    std::cout << "Solution: " << largest_prime_factor(n) << std::endl;
    return 0;
}
