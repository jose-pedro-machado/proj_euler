# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-
# valued terms.

def get_fibonacci_below_something(something: int):
    """ gets all the fibonacci number below something

    Args:
        something (int): number to show the upper bound of fibonacci number
    Returns:
        list of int: contains all fibonacci numbers below something

    """

    fibo_nums = [1, 1]

    bigger_than_something = False

    while not bigger_than_something:

        next_one = get_next_fibo_number(fibo_nums=fibo_nums)
        if next_one > something:
            bigger_than_something = True
        else:
            fibo_nums.append(next_one)

    return fibo_nums


def get_next_fibo_number(fibo_nums: list):
    """
    Args:
        fibo_nums (list of int): list with the current fibonacci numbers

    Returns:
        int: the next fibonacci number
    """

    return fibo_nums[-1] + fibo_nums[-2]


if __name__ == "__main__":
    something = int(4e6)

    fibo_nums = get_fibonacci_below_something(something=something)

    even_ones = [current_num
                 for current_num in fibo_nums
                 if current_num % 2 == 0]

    print("The sum of the even number on fibonacci sequence below " + str(something) + ' is: ' + str(sum(even_ones)))
