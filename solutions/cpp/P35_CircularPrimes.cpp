#include <cstring>
#include <iostream>
#include <string>
#include "euler_util\PrimeCache.hpp"

unsigned int count_circular_primes(prime_t max) {
    PrimeCache primes;
    unsigned int circular_prime_count = 0;
    for (auto p = primes.begin(); *p < max; ++p) {
        bool is_circular_prime = true;
        prime_t n = *p;
        std::string s_n = std::to_string(n);
        for (unsigned int i = 0; i < s_n.size(); ++i)  {
            if (!primes.contains(n)) {
                is_circular_prime = false;
                break;
            }
            s_n = s_n.substr(1) + s_n.substr(0, 1);
            n = std::stoll(s_n);
        }
        if (is_circular_prime) {
            ++circular_prime_count;
        }
    }
    return circular_prime_count;
}

int main(int argc, char **argv) {
    prime_t max = argc == 1 ? 1000000 : atoll(argv[1]);
    std::cout << "Solution: " << count_circular_primes(max) << std:: endl;
    return 0;
}