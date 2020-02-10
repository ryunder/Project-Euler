def findPalindromicNumbers(x, y):
    ''' Find the largest palindromic number between x and y.
        Palindromic numbers: 101, 1001, 11011, etc.'''
    nums = [x,y]
    palindromes = []
    for i in range(max(nums), min(nums), -1):
        for j in range(max(nums), min(nums), -1):
            a = str(i*j)
            if len(a) % 2 == 0:
                if a[0:len(a)//2] == a[:(len(a)//2)-1:-1]:
                    palindromes.append(int(a))                    
            else:
                if a[0:len(a)//2] == a[:(len(a)//2):-1]:
                    palindromes.append(int(a))

    return max(palindromes)

            
print(findPalindromicNumbers(99, 1000))            
    

