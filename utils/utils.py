import math


def get_all_divisors(number: int):
    """ Gets all the divisors of a given number

    Args:
        number (int): number to be extracted all its divisors
    Returns:
        list of int: contains all of the number divisors
    """
    divisors = []
    for divisor in range(2, math.ceil(number / 2) + 1):
        if number % divisor == 0:
            divisors.append(divisor)

    return divisors


def get_all_prime_divisors(number: int):
    """ Gets all the prime divisors of a given number

    Args:
        number (int): number to be extracted all its prime divisors
    Returns:
        list of list int: contains all of the number prime divisors, with the prime in the first position and its
            factor on the second
    """

    prime_divisors = []

    incrementing_divisor = 2
    # loop to keep dividing the number
    while number != 1:

        if number % incrementing_divisor == 0:
            current_divisor_factor = [incrementing_divisor, 0]

            # while the number can be divided by the divisor, keep dividing
            while number % incrementing_divisor == 0:
                number = number / incrementing_divisor
                current_divisor_factor[1] += 1

            prime_divisors.append(current_divisor_factor)

        incrementing_divisor += 1

    return prime_divisors


def is_it_prime(number: int):
    """ Verifies if the number is prime

    Args:
        number:
    Returns:
         bool: indicates if it is prime
    """
    # All the possible divisors of a number are between 2 and its square root
    for possible_divisor in range(2, math.ceil(math.sqrt(number))):
        if number % possible_divisor == 0:
            return False
        else:
            continue
    return True


def get_all_primes_until_something(number: int):
    """ Returns all the primes until the

    Args:
        number (int): ceiling to all primes vector
    Returns:
        list of int: all the primes until given number
    """

    primes = []

    for current_number in range(2, number + 1):
        if is_it_prime(number=current_number):
            primes.append(current_number)

    return primes