#include <algorithm>
#include <cmath>
#include <iostream>

#include "primes.hpp"

namespace primes {
  inline prime_t sqrt_ceil(prime_t n) {
    prime_t x = (prime_t) ceil(sqrt(n));
    while (x * x < n) {
      ++x;
    }
    return x;
  }
}

using namespace primes;

prime_cache::prime_cache() : prime_store({ 2, 3, 5, 7 }) {
}

bool prime_cache::contains(prime_t const n) {
  prime_t last = *prime_store.rbegin();
  if (n <= last) {
    return std::binary_search(prime_store.begin(), prime_store.end(), n);
  }
  else {
    prime_t const limit = sqrt_ceil(n);
    while (*prime_store.rbegin() < limit) {
      find_next();
    }
    for (auto p : prime_store) {
      if (limit < p) {
        break;
      }
      if ((n % p) == 0) {
        return false;
      }
    }
    return true;
  }
}

bool prime_cache::contains(signed long long const n) {
  return n < 0 ? false : this->contains((prime_t) n);
}

prime_iterator prime_cache::begin() {
  return prime_iterator(*this, 0);
}

prime_end_iterator prime_cache::end() {
  return prime_end_iterator();
}

void prime_cache::find_next() {
  prime_t curr = *(this->prime_store.rbegin());
  bool found_prime = false;
  do {
    curr += 2;
    prime_t const sqrt_curr = sqrt_ceil(curr);
    for (auto p = prime_store.begin(); p != prime_store.end(); ++p) {
      if ((curr % *p) == 0) {
        break;
      }
      else if (sqrt_curr < *p) {
        found_prime = true;
        break;
      }
    }
  } while (!found_prime);
  
  prime_store.push_back(curr);
}

prime_t prime_cache::get_at_index(size_t index) {
  while (prime_store.size() <= index) {
    find_next();
  }
  return prime_store[index];
}

prime_iterator::prime_iterator(prime_cache& primes, size_t index) : primes(primes) {
  this->index = index;
}

prime_t prime_iterator::operator*() {
  return primes.get_at_index(index);
}

prime_iterator prime_iterator::operator++() {
  return prime_iterator(primes, ++index);
}

prime_iterator prime_iterator::operator++(int) {
  prime_iterator current = prime_iterator(primes, index++);
  return current;
}

bool operator==(prime_iterator const& l, prime_iterator const& r) {
  return l.index == r.index;
}
bool operator==(prime_iterator const&, prime_end_iterator const&) {
  return false;
}
bool operator==(prime_end_iterator const&, prime_iterator const&) {
  return false;
}
bool operator==(prime_end_iterator const& l, prime_end_iterator const& r) {
  return true;
}
bool operator!=(prime_iterator const& l, prime_iterator const& r) {
  return !(l == r);
}
bool operator!=(prime_iterator const&, prime_end_iterator const&) {
  return true;
}
bool operator!=(prime_end_iterator const&, prime_iterator const&) {
  return true;
}
bool operator!=(prime_end_iterator const& l, prime_end_iterator const& r) {
  return false;
}

primes::prime_cache primes::primes;
