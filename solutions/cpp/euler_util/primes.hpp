#include <memory>
#include <vector>

#ifndef PRIMES_HPP
#define PRIMES_HPP

namespace primes {
  typedef unsigned long long prime_t;
  class prime_cache;
  class prime_iterator;
  class prime_end_iterator;
  extern prime_cache primes;
}

bool operator==(primes::prime_iterator const&, primes::prime_iterator const&);
bool operator==(primes::prime_iterator const&, primes::prime_end_iterator const&);
bool operator==(primes::prime_end_iterator const&, primes::prime_iterator const&);
bool operator==(primes::prime_end_iterator const&, primes::prime_end_iterator const&);
bool operator!=(primes::prime_iterator const&, primes::prime_iterator const&);
bool operator!=(primes::prime_iterator const&, primes::prime_end_iterator const&);
bool operator!=(primes::prime_end_iterator const&, primes::prime_iterator const&);
bool operator!=(primes::prime_end_iterator const&, primes::prime_end_iterator const&);

class primes::prime_cache {
  public:
    prime_cache();
    bool contains(prime_t const n);
    bool contains(signed long long const n);
    prime_iterator begin();
    prime_end_iterator end();
  private:
    std::vector<prime_t> prime_store;
    void find_next();
    prime_t get_at_index(size_t index);
  
  friend class primes::prime_iterator;
};

class primes::prime_iterator {
  public:
    prime_t operator*();
    prime_iterator operator++();
    prime_iterator operator++(int);
  private:
    prime_iterator(prime_cache&, size_t);
    prime_cache& primes;
    size_t index;
  
  friend class primes::prime_cache;
  friend bool ::operator==(prime_iterator const&, prime_iterator const&);
};

class primes::prime_end_iterator {
  private:
    prime_end_iterator() = default;
  friend class primes::prime_cache;
};

#endif
