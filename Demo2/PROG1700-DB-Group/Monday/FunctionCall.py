# Global variables area:
varOne = "Global Variable"

def main():
    myBalance = 500
    print(myBalance)

    secondFunction(10,20)

def secondFunction(par1, par2):
    result = par1 + par2

    varTwo = "Inside Second Function"

    varThree = "Yousef"
    #varOne=3
    print(varOne)
    print(varTwo)
    print(varThree)
    print(result)
    return
#print(result)

print(varOne)


main()