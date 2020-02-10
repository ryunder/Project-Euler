cache = {}
s = 0
x = 1
i = 0
even_fibs = []

def fib(n):

    if n in cache:
        return cache[n]
    
    if n == 0:
        result = 1
    elif n == 1 or n == 2:
        result = 1
    else:
        result = (fib(n-1) + fib(n-2))

    cache[n] = result
    return result
        

while i < 4000000:
    if i % 2 == 0:
        even_fibs.append(i)
    i = fib(x)
    x += 1

print(sum(even_fibs))
