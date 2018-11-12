#include <vector>

#ifndef PRIMES_HPP
#define PRIMES_HPP

typedef unsigned long long prime_t;

class PrimeCache {
	friend class PrimeIterator;
	public:
		PrimeCache();
		bool contains(prime_t);
		bool contains(signed long long);
		PrimeIterator begin();
	private:
		std::vector<prime_t> _primes;
		void find_next();
		void find_primes_to(prime_t);
		unsigned int find_prime_index(unsigned int start, unsigned int end, prime_t x);
		prime_t get_at_index(unsigned int);
};

class PrimeIterator {
	public:
		PrimeIterator(PrimeCache *, unsigned int);
		prime_t operator*();
		PrimeIterator operator++();
		PrimeIterator operator++(int);
	private:
		PrimeCache * const _source;
		unsigned int _index;
};

#endif