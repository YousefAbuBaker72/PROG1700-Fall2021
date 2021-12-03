stNames = []
pythonCourse = []
dbCourse = []

nOfStudents = int(input("How many number of students : "))
print("Enter students' names and marks for the {0} students".format(nOfStudents))
for i in range(nOfStudents):
    stName = input("Enter student's name # {0}\t: ".format(i+1))
    stNames.append(stName)
    pythonM = float(input("Enter {0}'s mark in python\t: ".format(stName)))
    pythonCourse.append(pythonM)
    dbmark = float(input("Enter {0}'s mark in DB\t: ".format(stName)))
    dbCourse.append(dbmark)

print("---------------------------------------------------")
print("StName\tPython Course\tData BaseCourse")
print("-------\t------------\t----------------")
for i in range(len(stNames)):
    print("{0}\t{1}\t\t{2}".format(stNames[i],pythonCourse[i],dbCourse[i]))
print("---------------------------------------------------")
print("The total mark of [python Course is : {0}, and Data Base course is : {1}]".format(sum(pythonCourse),sum(dbCourse)))
print("The average of [python Course is : {0:.2f}, and Data Base course is : {1:.2f}]".format(sum(pythonCourse)/nOfStudents,sum(dbCourse)/nOfStudents))
pythonAv=sum(pythonCourse)/len(pythonCourse)
dbAv=sum(dbCourse)/len(dbCourse)
print("----------------The First Report----------------")
print("Studnets' Marks less that Average in DB courses")
for i in range(len(stNames)):
    if dbCourse[i]<dbAv :
        print("{0} got\t{1} for Data Base Course".format(stNames[i],dbCourse[i]))
print("----------------The Second Report----------------")
print("Studnets' Marks who were suported in Python courses")
for i in range(len(stNames)):
    if pythonCourse[i]<60 :
        pythonCourse[i] +=5
        print("{0} got\t{1} in Python".format(stNames[i],pythonCourse[i]))
print("----------------The Third Report----------------")
print("Studnets' names before sorted in ascending order")
print(stNames)
print("Studnets' names after sorted in ascending order")
stNames.sort()
print(stNames)
