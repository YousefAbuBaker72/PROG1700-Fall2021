
def functionLoop():
    sum=0
    counter=0
    while counter<10:
        sum=sum+counter
        print("counter= ",counter)
        # counter = counter+1
        counter +=1
    print("the total sum from While loop is : ",sum)

functionLoop()

### Another function
print("The second function results")
def functionLoopTwo(nParameter):
    sum=0
    counter=0
    while counter<nParameter:
        sum=sum+counter
        print("counter= ",counter)
        # counter = counter+1
        counter +=1
    print("the total sum from While loop is : ",sum)

n = int(input("Enter the value of n : "))
functionLoopTwo(n)

### Another Third function
print("The third function results")
def functionLoopThree(nValue):
    sum=0
    counter=0
    while counter<nValue:
        sum=sum+counter
        print("counter= ",counter)
        # counter = counter+1
        counter +=1
    return sum
m = int(input("Enter the value of m : "))
theResult = functionLoopThree(m)
print("the total sum from While loop is : ",theResult)
print("the total sum from While loop is : ",functionLoopThree(m))

