from math import sqrt
import time

pythTriples = []
squares = [x*x for x in range(1, 1000)]


for i in range(len(squares)-2):
    for j in range(i+1, len(squares)-1):
        a = squares[i]
        b = squares[j]
        if a + b in squares:
            pythTriples.append((sqrt(a), sqrt(b), sqrt(a+b)))           


for i in range(len(pythTriples)):
    if sum(pythTriples[i]) == 1000:
        print(pythTriples[i], pythTriples[i][0]*pythTriples[i][1]*pythTriples[i][2])

