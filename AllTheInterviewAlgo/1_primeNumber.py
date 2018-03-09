def replaceNo(number, position, replaceNo):
    lsb = number%pow(10,position)
    msb= int(number/pow(10,position+1))
    newNo = msb*pow(10,position+1) + replaceNo * pow(10,position) + lsb
    return newNo

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

def main():
    numberN = int(input("Enter any number="))
    len1=len(str(numberN))
    i=len1-1
    j=0
    k=0
    #positionChange A loop
    lowestPrimeNo = None
    steps=0
    while i>=1:
        for aNo in range(1,10): #Change no loop
            #temp = getNumberList(numberN)
            temp =  replaceNo(numberN,i,aNo)
            if lowestPrimeNo != None and lowestPrimeNo < temp:
                continue
            j=i-1
            #Position Change B loop
            while j>=0:
                temp1 = temp
                for bNo in range(1,10):
                    temp1=replaceNo(temp,j,bNo)
                    if lowestPrimeNo != None and lowestPrimeNo < temp1:
                        continue
                    if lowestPrimeNo == None:
                        if isPrimerNumber(temp1):
                            lowestPrimeNo = temp1
                    if isPrimerNumber(temp1):
                        if not lowestPrimeNo:
                           lowestPrimeNo = temp1
                        elif lowestPrimeNo > temp1:
                            lowestPrimeNo = temp1
                    steps += 1
                    #print(temp1)
                j -= 1
        i -= 1
    print("Total steps= %s" % steps)
    print("Lowest prime number=%s" % lowestPrimeNo)
#Number change A

#position change B
#Number change B

main()