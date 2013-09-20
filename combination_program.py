from math import factorial

def nCr(n, k):
	return int(factorial(n)/(factorial(k)*factorial(n - k)))

print(nCr(8, 4))