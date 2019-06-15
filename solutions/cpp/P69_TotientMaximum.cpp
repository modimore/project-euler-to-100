#include <iostream>
#include <sstream>
#include "euler_util/number_theory.hpp"

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
