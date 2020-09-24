from utils.utils import is_it_prime

if __name__ == "__main__":

    number_of_primes = 0
    iterating_number = 1

    while number_of_primes < 10001:

        iterating_number += 1

        if is_it_prime(iterating_number):
            number_of_primes += 1

    print (iterating_number)