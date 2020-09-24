if __name__ == '__main__':

    number = 100

    # loop to get the sum of squares of all numbers until numer
    sum_of_square = 0
    for num in range(1, number + 1):
        sum_of_square += num ** 2

    # loop to get the square of the sum of all numbers until number
    square_of_sum = sum(range(number + 1))
    square_of_sum = square_of_sum ** 2

    result = square_of_sum - sum_of_square

    print("The result is, for the first " + str(number) + " numbers: " + str(result))
