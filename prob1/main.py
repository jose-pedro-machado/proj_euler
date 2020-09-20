
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def find_multiples_3_5(num: int):
    """ Finds the multiples of 3 and 5 for below the given input
        Args:
            num (int): integer to be encountered all multiples

        Returns:
            list of int: contains all the multiples of 3 and 5 below num
    """

    multiples = []

    for current_num in range(num):

        if current_num % 15 == 0:
            multiples.append(current_num)

        elif current_num % 3 == 0:
            multiples.append(current_num)

        elif current_num % 5 == 0:
            multiples.append(current_num)

    return multiples

if __name__ == "__main__":

    number = 1000

    multiples = find_multiples_3_5(num=number)

    result = sum(multiples)

    print("The sum of all multiples of 3 and 5 below " + str(number) + ' is: ' + str(result))