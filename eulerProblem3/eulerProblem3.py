import numpy as np

# Define the original polynomial
def u(n):
    return sum([(-1) ** k * n ** k for k in range(11)])

terms = [u(n) for n in range(1, 12)]
# Generate first 11 terms
fit_sum = 0

for k in range(1, 11):
    x = np.arange(1, k + 1)
    y = terms[:k]
    print ("Fitting polynomial to first", k, "terms:", y)

    # Fit polynomial of degree k-1
    coeffs = np.polyfit(x, y, deg=k - 1)
    print("Coefficients:", coeffs)
    poly = np.poly1d(coeffs)
    print("Fitted polynomial:", poly)

    # Predict next term
    predicted = round(poly(k + 1))
    actual = terms[k]

    if predicted != actual:
        print("Predicted FIT for k =", k, "is", predicted, "while actual is", actual)
        fit_sum += predicted

print("Sum of FITs:", fit_sum)








