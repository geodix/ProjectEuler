"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 5 x 5 =25; it is also an odd square.

The first 5 square numbers are: 1,4,9,16,26
, and the sum of the odd squares is 1+9+25 = 35
.

Among the first 162 thousand square numbers, what is the sum of all the odd squares?


Formula for Sum of squares of n natural numbers: [n(n+1)(2n+1)] / 6.
Formula for Sum of squares of first n even numbers: [2n(n + 1)(2n + 1)] / 3.
Formula for Sum of squares of first n odd numbers: [n(2n+1)(2n-1)] / 3.

"""

def sum_of_odd_squares(limit):
    n = int(limit*0.5)  # Find the largest integer whose square is <= limit
    sum_odd_squares = (n * (2*n + 1) * (2*n - 1)) // 3  # Sum of squares of first n odd numbers
    return sum_odd_squares


result = sum_of_odd_squares(162000)
print(result)
