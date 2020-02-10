import time

start = time.time()

def collatz_step(n):
    if n == 1:
        return int(n)
    elif n%2:
        n = 3*n + 1
        return int(n)
    else:
        n = n/2
        return int(n)

def collatz(num): 
    chain = [num]

    while num != 1:
        num = collatz_step(num)
        chain.append(num)

    return chain

max_chain = 0
max_chain_n = 0
for x in range(1, 1000000):
    chain_len = len(collatz(x))
    if chain_len > max_chain:
        max_chain = chain_len
        max_chain_n = x
    if not x % 100000:
        print(x, max_chain_n, max_chain)
        print(time.time()-start)

print('DONE', max_chain_n, max_chain)
print(time.time()-start)   
