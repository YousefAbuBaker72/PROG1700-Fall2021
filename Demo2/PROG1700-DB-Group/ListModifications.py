#           0  1   2    3  4
stMarks = [99, 75, 30, 40, 76]

print(stMarks)
       
print("The total number of elements is : ", len(stMarks))
for i in range(len(stMarks)):
    print(stMarks[i])
print(stMarks[-1])
print(stMarks[-2])


# foreach loop
# for each element in the list
print("From the foreach loop")

for mark in stMarks: # mark is the variable that will save inside it 
    # each element from the list per iteration.   
    print(mark)
print("Declaring an empty list : ")
stNames = []
# stNames.append("Yousef")
# print(stNames)
# stNames.append("Sam")
# print(stNames)
# stNames.append("Daniel")
# print(stNames)
print("The largest mark is : ", max(stMarks))
print("The lowest mark is : ", min(stMarks))
# Adding new Elements Using loop
# maxValue=0
# nummberOfStudents = int(input("How many number of students : "))
# for i in range(nummberOfStudents):
#     stName= input("Enter student name : ")
#     stNames.append(stName)
# print("The students' names are : ")
# print(stNames)
# print(stMarks)


# Not related to List
evenNumbers=0
for i in range(10):
    if i%2==0:
        evenNumbers = evenNumbers+1
        print("{0} is even number".format(i))
print("Theb total number of even numbers is : ",evenNumbers)



     
 

