def getUnitDigit(num):
    return num % 10

def printSumOfDigits(num):
    total = 0
    while num > 0:
        total += (num % 10)
        num //= 10
    print(total)

def printProductOfDigits(num):
    product = 1
    while num > 0:
        product *= (num % 10)
        num //= 10
    print(product)

def getLargestDigit(num):
    return max([int(digit) for digit in str(num)])

def getSmallestDigit(num):
    return min([int(digit) for digit in str(num)])

num = int(input())
print(getUnitDigit(num))
printSumOfDigits(num)
printProductOfDigits(num)
print(getLargestDigit(num))
print(getSmallestDigit(num))
