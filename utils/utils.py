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
        list of int: contains all of the number prime divisors
    """

    # TODO (José) Still not right. Test to find all divisors and all prime divisors for 10001 and find out
    prime_divisors = []

    for prime_divisor in range(2, math.floor(math.sqrt(number))):
        if number % prime_divisor == 0:
            if is_it_prime(number=prime_divisor):
                prime_divisors.append(prime_divisor)
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

if __name__ == "__main__":

    number = 10001

    a = get_all_prime_divisors(number=number)
    n = get_all_divisors(number=number)

    a = 0