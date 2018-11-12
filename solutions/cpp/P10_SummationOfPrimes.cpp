#include <iostream>
#include "euler_util\PrimeCache.hpp"

unsigned long long summation_of_primes_to(unsigned long long max) {
    unsigned long long sum = 0;
    PrimeCache primes;
    PrimeIterator p = primes.begin();
    while (*p < max)
        sum += *(p++);
    return sum;
}

int main() {
    unsigned long long max = 2000000;
    std::cout << "Solution: " << summation_of_primes_to(max);
    return 0;
}