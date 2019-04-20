#include <iostream>
#include <sstream>
#include "euler_util/PrimeCache.hpp"

PrimeCache primes;

unsigned long long gcd(unsigned long long a, unsigned long long b) {
    if (b == 0) return a;
    if (a < b) return gcd(b, a);
    return gcd(b, a%b);
}

unsigned int phi(unsigned long long n) {
    if (n == 1)
        return 1;
    if (primes.contains(n))
        return n-1;
    
    unsigned int r = 1;
    PrimeIterator p = primes.begin();
    while (*p <= n) {
        if (n%*p == 0) {
            n = n / *p;
            unsigned long long g = gcd(n, *p);
            r = r * phi(*p) * g / phi(g);
        }
        else {
            p++;
        }
    }
    
    return r;
}

int main(int argc, char** argv) {
    unsigned long long limit = 1000000;
    if (argc > 1) {
        std::stringstream(argv[1]) >> limit;
    }
    
    unsigned long long best = 1;
    float best_f = 1.0f;
    
    for (unsigned long long n=2; n <= limit; ++n) {
        const float f = float(n) / phi(n);
        if (f > best_f) {
            best_f = f;
            best = n;
        }
    }
    
    std::cout << best << std::endl;
    
    return 0;
}
