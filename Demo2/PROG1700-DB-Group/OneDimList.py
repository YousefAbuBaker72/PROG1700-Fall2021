stMarks=[10, 20, 55, 88, 99, 100]
print(stMarks)
for i in range(6):
    print(stMarks[i])
for i in range(len(stMarks)):
    print(stMarks[i])
# Modifying the list elements

stMarks[0] = -999
print("stMarks after update")
for i in range(len(stMarks)):
    print(stMarks[i])




print("The maximum value of those marks")
print(max(stMarks))

print("The minimum value of those marks is : ",min(stMarks))

# Adding elements to the list:
stMarks.append(44)
print("The list after updating :")
for i in range(len(stMarks)):
    print(stMarks[i])

print(stMarks)
stMarks.insert(2,11111)
print(stMarks)
for i in range(len(stMarks)):
    print(stMarks[i])

stMarks.remove(-999)

print(stMarks)
stMarks.remove(11111)
print(stMarks)

stNames = []
stNames.append("Yousef")
stNames.append("David")
stNames.append("Mary")
#stNames[0] = "yousef" # Modifying the first element. 
print(stNames)
print("From function")

def func1(stN):
    stN.append("Felix")
    for i in range(len(stN)): 
        print(stN[i])
func1(stNames)
print(stNames)








