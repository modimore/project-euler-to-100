#include "PrimeCache.hpp"

#include <algorithm>
#include <cmath>

PrimeCache::PrimeCache() {
	this->_primes = std::vector<prime_t> {2, 3, 5, 7};
}

bool PrimeCache::contains(prime_t x) {
	if (x == 1) { return false; }
	prime_t sqrt_x = sqrt(x);
	if (*this->_primes.rbegin() < sqrt_x) {
		this->find_primes_to(sqrt_x);
	}
	for (auto p = this->begin(); *p <= sqrt_x; ++p) {
		if (x % *p == 0) {
			return false;
		}
	}
	return true;
	// if (*this->_primes.rbegin() < x) {
	// 	this->find_primes_to(x);
	// }
	// return this->find_prime_index(0, this->_primes.size(), x) != this->_primes.size();
}

bool PrimeCache::contains(signed long long x) {
	return x < 0 ? false : this->contains((prime_t) x);
}

PrimeIterator PrimeCache::begin(void) {
	return PrimeIterator(this, 0);
}

void PrimeCache::find_next() {
	prime_t current = *(this->_primes.rbegin());
	bool is_prime;
	do {
		current += 2;
		is_prime = true;
		
		for (auto p = this->_primes.begin(); p != this->_primes.end(); ++p) {
			if ((current % *p) == 0) {
				is_prime = false;
				break;
			}
			else if ((*p) * (*p) > current) {
				break;
			}
		}
	} while (!is_prime);
	
	this->_primes.push_back(current);
}

void PrimeCache::find_primes_to(prime_t x) {
	while (*this->_primes.rbegin() < x) {
		this->find_next();
	}
}

unsigned int PrimeCache::find_prime_index(unsigned int start, unsigned int end, prime_t x) {
	if (end == start + 1) {
		return this->_primes[start] == x ? start : this->_primes.size();
	}
	unsigned int mid = (start + end) / 2;
	return x < this->_primes[mid] ? this->find_prime_index(start, mid, x) : this->find_prime_index(mid, end, x);
}

prime_t PrimeCache::get_at_index(unsigned int index) {
	while (this->_primes.size() <= index) {
		this->find_next();
	}
	return this->_primes[index];
}

PrimeIterator::PrimeIterator(PrimeCache * primes, unsigned int index)
	: _source(primes), _index(index) {}

prime_t PrimeIterator::operator*() {
	return this->_source->get_at_index(this->_index);
}

PrimeIterator PrimeIterator::operator++() {
	++(this->_index);
	return (*this);
}

PrimeIterator PrimeIterator::operator++(int) {
	return PrimeIterator(this->_source, (this->_index)++);
}
