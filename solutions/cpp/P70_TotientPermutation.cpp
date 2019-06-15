#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <sstream>
#include "euler_util/primes.hpp"

using primes::prime_t;

bool is_permutation(unsigned long long m, unsigned long long n) {
	std::string s_m = std::to_string(m);
	std::string s_n = std::to_string(n);
	
	s_m.resize(std::max(s_m.size(), s_n.size()), '0');
	s_n.resize(std::max(s_m.size(), s_n.size()), '0');
	std::sort(s_m.begin(), s_m.end());
	std::sort(s_n.begin(), s_n.end());
	return s_m == s_n;
}

int main(int argc, char ** argv) {
	using primes::primes;
	
	unsigned long long limit = 1E7;
	if (argc > 1) {
		std::stringstream(argv[1]) >> limit;
	}
	
	unsigned long long best_n = 1;
	float best_f = std::numeric_limits<float>::infinity();
	
	for (auto pi1 = primes.begin(); *pi1 < limit; ++pi1) {
		for (auto pi2 = primes.begin(); *pi2 < *pi1; ++pi2) {
			prime_t p1 = *pi1, p2 = *pi2;
			unsigned long long n = p1 * p2, phi = (p1-1) * (p2-1);
			
			if (n > limit)
				break;
			
			float f = (float) n / phi;
			if (f < best_f && is_permutation(n, phi)) {
				best_f = f;
				best_n = n;
			}
		}
	}
	
	std::cout << "Solution: " << best_n << std::endl;
}
