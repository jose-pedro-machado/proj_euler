# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from utils.utils import get_all_prime_divisors

if __name__ == "__main__":
    something = 600851475143

    divisors = get_all_prime_divisors(number=something)
    print(divisors)
