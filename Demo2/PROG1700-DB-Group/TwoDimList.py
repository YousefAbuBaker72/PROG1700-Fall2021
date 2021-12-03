my2dList = []


my2dList.append([1,2,3,4]) # row number 0
my2dList.append([4,5,6,7]) # row # 1
my2dList.append([8,9,10,11]) # row # 2
my2dList.append([10,20,30,40]) # row # 3

print(my2dList)
#   my2dList[RowIndex][ColumnIndex]
my2dList[2][1] = 999
print(my2dList)

# foreach loop
print("Printing the list using foreach loop")
for row in my2dList:
    print(row)

# Nested foreach loop
print("Printing the list using nested foreach loop")
for row in my2dList: # get the list row by row
    for element in row: # column represent fisrt value in row List at the first 
           # iteration. Then 
        print(element) # the default value of end is '\n'; new Line

print("Printing the list using nested foreach loop in nicely way")
for row in my2dList: # get the list row by row
    for column in row: # column represent fisrt value in row List at the first 
           # iteration. Then 
        print(column , end = " ")

print("\nPrinting the list using nested foreach loop in perfect way")
for row in my2dList: # get the list row by row
    for column in row: # column represent fisrt value in row List at the first 
           # iteration. Then 
        print(column , end = " ")
    print() # New Line separator
print("The len of my2dList is : " ,len(my2dList))
print("\nPrinting the list using nested for loop in perfect way")
for rowIndex in range(len(my2dList)): # get the list row by row
    for columnIndex in range(len(my2dList[rowIndex])): # column represent fisrt value in row List at the first 
           # iteration. Then 
        print(my2dList[rowIndex][columnIndex], end = " ")
    print()   

