#include <cstdlib>
#include <iostream>
#include "euler_util\PrimeCache.hpp"

unsigned int problem_58(double ratio_limit) {
    PrimeCache primes;
    unsigned long long value = 1;
    unsigned int step = 0;
    double ratio = 1.0;
    unsigned int n_primes = 0, n_values = 1;
    
    while (ratio > ratio_limit) {
        step += 2;
        if (primes.contains(value += step)) n_primes += 1;
        if (primes.contains(value += step)) n_primes += 1;
        if (primes.contains(value += step)) n_primes += 1;
        value += step;
        n_values += 4;
        ratio = (double) n_primes / n_values;
    }
    
    return step + 1;
}

int main(int argc, char **argv) {
    double ratio_limit = argc == 1 ? 0.10 : atof(argv[1]);
    std::cout << "Solution: " << problem_58(ratio_limit) << std::endl;
    return 0;
}