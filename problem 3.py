def factorize(num):
    factors = []
    i = 2
    while i * i <= num:
        if (num % i):          
            i += 1
        else:
            factors.append(i)
            num //= i

    if num > 1:
        factors.append(num)
    
    return factors

print(factorize(600851475143))
