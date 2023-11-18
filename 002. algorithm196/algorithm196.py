## lychrel number (196-algorithm)

## A Lychrel number is a natural number
## that cannot form a palindrome
## through the iterative process of
## repeatedly reversing its digits and
## adding the resulting numbers.
## This process is sometimes called the 196-algorithm.
## For example, 56 and 125 are not Lychrel numbers
## 56 + 65 = 121
## 125 + 521 = 646
## Some numbers become palindromes quickly after
## repeated reversal and addition,
## and are therefore not Lychrel numbers.
## All one-digit and two-digit numbers
## eventually become palindromes after repeated reversal and addition.

## The task is to find if a given number is Lychrel
## with a given limit on the number of iterations.


print('#' * 50)
print()
print('This program checks whether the entered number is Lychrel number or not.')
print('_' * 30)
n1 = int(input('Number is '))
print('_' * 30)

actual_n = n1

## limit of iterations is set to 1000 iterations
for i in range(1, 1_000): 

    n1 = str(n1)
    n2 = n1[::-1]

    n2 = int(n2)
    n1 = int(n1)

    res = n1 + n2
    res = str(res)
    print('|', i, '|', res)
    
    if res == res[::-1]:
        print('_' * 50)
        print('Palindromic number : {}'.format(res))
        print('_' * 50)
        print('Number of iterations : {}'.format(i))
        print('_' * 50)
        print('{} is not a Lychrel number'.format(actual_n))
        print('_' * 50)
        break
    else:
        res = int(res)
        n1 = res
        continue
else:
    print('_' * 50)
    print('Number of iterations : {}'.format(i))
    print('_' * 50)
    print('_' * 50)
    print('{} is a Lychrel number'.format(actual_n))
    print('_' * 50)
print()
## _______________________________________________________
## Biggest NOT Lychrel number is 1000206827388999999095750,
## it has 293 iterations.
## lychrel numbers are 196, 879, 1997, 7059
## _______________________________________________________
##

## for screen not to close when operation is finished
input("Press any key to close...") 
