# Write a program for:
# Given 5 digit number  , modify any to digits to return highest and lowest prime number

def isPrimerNumber(number):
    if number == 0:
        print("Zero is not a prime number")
        return False
    if number == 2:
        return True
    if number == 3:
        return True
    if number%2 == 0:
        return False
    if number%3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def getAllNumbersInArray(number):
   #pythonic
   #convert first into string
   x1=str(number)
   #convert into string array
   x2=list(x1)
   #convert back to in array
   x3=list(map(int, x2))
   return x3

def generatorFunc():
    for i in range(99,10,-1):
        x1=str(i)
        if '0' in x1:
            continue
        else:
            yield(i)

def programForLargestPN(number):
    x3=getAllNumbersInArray(number)
    y1=generatorFunc()
    for i in y1:
       numberToCheck= x3[4]*10000+x3[3]*1000+ x3[2]*100+ i
       if isPrimerNumber(numberToCheck):
           print("Number %s is the largest prime number", numberToCheck)
           return

def main():
    number=int(input("Enter 5 digit number="))
    programForLargestPN(number)

if __name__ == '__main__':
    main()