class Numbers:
    def __init__(self,Number):
        self.Value = Number

    def ChkPrime(self):
        count = 0

        for i in range(2,self.Value):
            if self.Value % i == 0:
                count = count + 1
                break
        
        if count == 1:
            return False
        else:
            return True
        
    def ChhPerfect(self):
        sum = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum = sum + i

        if sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are : ")
        for i in range(1,self.Value):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        sum1 = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                sum1 = sum1 + i

        return sum1
    
def main():
    bRet1 = False
    bRet2 = False
    Ret = 0

    obj1 = Numbers(12)
    print(12,":")
    bRet1 = obj1.ChkPrime()
    if bRet1 == True:
        print("It is prime number")
    else:
        print("Not a prime number")
    
    bRet2 = obj1.ChhPerfect()
    if bRet2 == True:
        print("It is perfect number")
    else:
        print("Not a perfect number")

    obj1.Factors()
    Ret = obj1.SumFactors()
    print("Sum of factor is :",Ret)
    
    print("")

    obj2 = Numbers(6)
    print(6,":")
    bRet1 = obj2.ChkPrime()
    if bRet1 == True:
        print("It is prime number")
    else:
        print("Not a prime number")
    
    bRet2 = obj2.ChhPerfect()
    if bRet2 == True:
        print("It is perfect number")
    else:
        print("Not a perfect number")

    obj2.Factors()
    Ret = obj2.SumFactors()
    print("Sum of factor is :",Ret)
    
    print("")
   
    obj3 = Numbers(13)
    print(13,":")
    bRet1 = obj3.ChkPrime()
    if bRet1 == True:
        print("It is prime number")
    else:
        print("Not a prime number")
    
    bRet2 = obj3.ChhPerfect()
    if bRet2 == True:
        print("It is perfect number")
    else:
        print("Not a perfect number")

    obj3.Factors()
    Ret = obj3.SumFactors()
    print("Sum of factor is :",Ret)
    
    print("")
   
if __name__ == "__main__":
    main()