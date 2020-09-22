
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
from utils.utils import is_palindrome

if __name__ == "__main__":

    # gets two 3 digit multiplying numbers. Multiply them and verify palindrome. Decrease one at a time

    # they must be n-digit numbers with all digits 9
    multiple_a = 999
    multiple_b = 999

    biggest_palindromes = {"palindrome": 0,
                           "multiple_a": 0,
                           "multiple_b": 0}
    for decrease_a in range(1, multiple_a - multiple_a // 10):
        for decrease_b in range(1, multiple_b - multiple_b // 10):
            testing_number = (multiple_a - decrease_a) * (multiple_b - decrease_b)
            if is_palindrome(number=testing_number):
                if testing_number > biggest_palindromes["palindrome"]:
                    biggest_palindromes = {"palindrome": testing_number,
                                           "multiple_a": multiple_a - decrease_a,
                                           "multiple_b": multiple_b - decrease_b}

    print("Biggest palindrome, made by a product of 2 3-digit numbers (" + str(biggest_palindromes["multiple_a"]) +
          " and " + str(biggest_palindromes["multiple_b"]) + "): " + str(biggest_palindromes['palindrome']))