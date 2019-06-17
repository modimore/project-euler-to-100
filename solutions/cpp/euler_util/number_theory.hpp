#ifndef NUMBER_THEORY_HPP
#define NUMBER_THEORY_HPP

template<class M, class N>
constexpr std::common_type_t<M, N> gcd(M m, N n);

unsigned long long phi(unsigned long long n);

#endif
