#include "number_theory.hpp"
#include "primes.hpp"

template<class M, class N>
constexpr std::common_type_t<M, N> gcd(M m, N n) {
    if (n == 0)
        return m;
    if (m < n)
        return gcd(n, m);
    return gcd(n, m%n);
}

unsigned long long phi(unsigned long long n) {
    if (n == 1)
        return 1;
    if (primes.contains(n))
        return n-1;
    
    unsigned int r = 1;
    auto p = primes::primes.begin();
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
