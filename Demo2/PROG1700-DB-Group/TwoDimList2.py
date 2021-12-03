empInfo = []
# empInfo = [["Yousef", 2000, "Halifax", 5],
 #           ["Abcd", 4000, "Antigonish", 3]
# ]


numOfEmp = int(input("Enter the number of employees : "))
for i in range(numOfEmp):
    tempInfo=[] # One Dim. List . It is going to empty the list in each iteratio
    empName = input("Enter the employee name ")
    empSalary = float(input("Employee salary "))
    empAdd = input("Enter the employee address ")
    numOfKids = int(input("Enter number of kids "))
    tempInfo.append(empName)
    tempInfo.append(empSalary)
    tempInfo.append(empAdd)
    tempInfo.append(numOfKids)
    empInfo.append(tempInfo)
#print(tempInfo)
print(empInfo)




