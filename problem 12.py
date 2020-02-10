import time, math

start = time.time()

'''
def triangleNumber(n):
    return sum(range(n+1))

def findDivisors(n):
    divs = [x for x in range(1, 1+int(n/2)) if not n%x]
    divs.append(n)
    return divs

x = 0
# tri_num = 0

while len(findDivisors(triangleNumber(x))) <= 500:
    x += 1
    # tri_num += x
    if x % 500 == 0:
        print(x, triangleNumber(x), len(findDivisors(triangleNumber(x))), time.time()-start)

print('x: ', x)
print('x_tri: ', triangleNumber(x))
print('total time: ', time.time()-start)

'''
# https://codereview.stackexchange.com/questions/83579/project-euler-problem-12-in-python
def divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors


for x in range(1, 100000):
    tri_num = (x*(x+1))/2
    if x%2 == 0:
        cnt = divisors(x/2)*divisors(x+1)
    else:
        cnt = divisors(x)*divisors((x+1)/2)
    if cnt >= 500:
        break

print('x: ', x)
print('x_tri: ', tri_num)
print('total time: ', time.time()-start)


    
