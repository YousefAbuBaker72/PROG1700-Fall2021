stNames = [] # this is the list variable
for i in range(5):
    stName = input("Enter student name : ")
    stNames.append(stName)
print(stNames)

def someFunction(stN):
    print(stN)
someFunction(stNames)


