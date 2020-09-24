from utils.utils import get_all_primes_until_something, get_all_prime_divisors, get_all_divisors

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
if __name__ == "__main__":
    number = 20
    primes_below_number = get_all_primes_until_something(number=number)
    all_prime_factor = [[prime, 1] for prime in primes_below_number]

    for current_number in range(2, number + 1):

        aux = get_all_prime_divisors(number=current_number)

        for current_number_divisors in aux:

            divisor_index = primes_below_number.index(current_number_divisors[0])

            if current_number_divisors[1] > all_prime_factor[divisor_index][1]:
                all_prime_factor[divisor_index][1] = current_number_divisors[1]

    result = 1
    for prime in all_prime_factor:
        result *= prime[0] ** prime[1]

    print("The smallest positive number that is evenly divisible by all of the numbers from "
          "1 to " + str(number) + " is: " + str(result))
