var1 = 5 # Global variable

def someFunction():
    #print(var1)
    
    var1 = 9 # Local variable
    var2=5
    print(var2)
    print(var1) # printing the global variable 
someFunction()
print(var2)
print(var1)
