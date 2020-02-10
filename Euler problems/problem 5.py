def isEvenlyDivisible(num, factors_limit):
    for factor in range(1, factors_limit+1):
        if num % factor:
            return False
    return True


#isEvenlyDivisible(2520, 10)

num = 2520
while True:
    if not isEvenlyDivisible(num, 20):
        num += 2520
        continue
    print(num)
    break

