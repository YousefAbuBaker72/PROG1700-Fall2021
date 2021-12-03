#         stName, stMarks, EyeColor, StEnrol.
# stInfo=[ ["Yousef", 95, "Black","Full Time"],
#           ["Brad", 70, "Brown", "Part Time"],
#           ["Geoff", 85, "Black", "Full Time"]
#         ]
# print(stInfo)

stNames = []
stMarks = []

# for i in range(3):
#     stName = input("Enter student's name : ")
#     stMark = float(input("Enter student's mark : "))
#     stNames.append(stName)
#     stMarks.append(stMark)

# print(stNames)
# print(stMarks)

# for i in range(3):
#     stName = input("Enter student's name # {0} : ".format(i+1))
#     stMark = float(input("Enter student's mark # {0} : ".format(i+1)))
#     stNames.append(stName)
#     stMarks.append(stMark)

# print(stNames)
# print(stMarks)

for i in range(3):
    stName = input("Enter student's name # {0} \t: ".format(i+1))
    stMark = float(input("Enter {0}'s mark #  \t\t: ".format(stName)))
    stNames.append(stName)
    stMarks.append(stMark)

print(stNames)
print(stMarks)

# Find the sum and average of students marks

print("The total sum of students' marks is : ", sum(stMarks))
print("The average is : {0:.2f}".format(sum(stMarks)/len(stMarks)))

# Print out (student name, mark) whose their mark is greater than or equal the average
average = sum(stMarks)/len(stMarks)
for i in range(len(stMarks)):
    if stMarks[i] >= average:
        print(stNames[i],"\t", stMarks[i])
print("The following fail the course : ")
for i in range(len(stMarks)):
    if stMarks[i] < 60:
        print(stNames[i],"\t", stMarks[i])
print("The following students passed the course by help : ")
for i in range(len(stMarks)):
    if stMarks[i] < 60:
        stMarks[i] = 60;
        print(stNames[i],"\t", stMarks[i])
