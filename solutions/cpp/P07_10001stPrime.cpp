#include <iostream>
#include "euler_util\primes.hpp"

unsigned long long nth_prime(unsigned int n) {
    using primes::primes;
    auto p = primes.begin();
    for (unsigned int i = 1; i < n; ++i) {
        ++p;
    }
    
    return *p;
}

int main(int argc, char **argv) {
    unsigned int n = 10001;
    std::cout << "Solution: " << nth_prime(n) << std::endl;
    return 0;
}
