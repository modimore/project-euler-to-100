#include <iostream>
#include "euler_util\primes.hpp"

unsigned long long summation_of_primes_to(unsigned long long max) {
    unsigned long long sum = 0;
    using primes::primes;
    for (auto p = primes.begin(); *p < max; ++p) {
      sum += *p;
    }
    return sum;
}

int main() {
    unsigned long long max = 2000000;
    std::cout << "Solution: " << summation_of_primes_to(max) << std::endl;
    return 0;
}
