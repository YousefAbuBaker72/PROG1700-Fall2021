
# Col.IndexVal.= 0, 1, 2,  3
my2DList = [    [1, 2, 3, 4],# First Row. Index value is 0
                [5, 6, 7, 8], # Secomd Row. Index value is 1
                [9,10,11,12] # Third Row. Index value is 2
                ]
print(my2DList)

print(len(my2DList))

print(my2DList[0])
print(my2DList[1])
print(my2DList[2])
#      
# my2DList[rowIndex][ColumnIndex]
print(my2DList[0][1])
print(my2DList[2][2])

my2DList2 = []

my2DList2.append([10,20,30,40]) # The first row
my2DList2.append([30,0,20,10]) # The second row
my2DList2.append([10,20,30,40]) # The 3rd row

#print(my2DList)
print(my2DList2)

# Using foreach loop:
print("Printing the 2 dim list using foreach loop :")
for row in my2DList2:
    print(row)

# Using foreach loop:
print("Printing the 2 dim list using nested foreach loop :")
for row in my2DList2:
    for column in row:
        print(column) # the default end = '\n' which means new Line

# Using foreach loop:
print("Printing the 2 dim list using nested foreach loop in nicely way-1 :")
for row in my2DList2:
    for column in row:
        print(column, end = ' ')

print("\nPrinting the 2 dim list using nested foreach loop in nicely way-2 :")
for row in my2DList2:
    for column in row:
        print(column, end = ' ')
    print()
print(len(my2DList2))
print(len(my2DList2[0]))       
print("\nPrinting the 2 dim list using nested for loop in a nicely way :")
for rowIndex in range(len(my2DList2)): # The row index : 0,1,2
    for columnIndex in range(len(my2DList2[rowIndex])): # The col index : 0,1,2,3
        print(my2DList2[rowIndex][columnIndex], end = ' ')
    print()