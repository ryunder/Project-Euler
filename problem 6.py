def sumOfSquares(n):
    sos = [i*i for i in range(n+1)]
    return sum(sos)

def squareOfSums(n):
    return sum(range(n+1))**2

def sumSquareDifference(n):
    print(squareOfSums(n) - sumOfSquares(n))


sumSquareDifference(100)
