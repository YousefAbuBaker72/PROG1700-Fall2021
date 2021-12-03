print("====================================")
print("===========First Method=============")
for i in range(10, -1, -1):
    if i ==0:
        print(i, " BLASTOFF!!")
    else:
        print(i)
print("====================================")
print("===========Second Method============")
runAgain = True
while runAgain:
    
    for i in range(10, -1, -1):
        if i ==0:
            print(i, " BLASTOFF!!")
        else:
            print(i)
    answerValue = input("Do you want to continue? (Y/N) ").upper()
    if answerValue =="N":
        runAgain = False
        print("Done. Thank you")

print("====================================")
print("============Third Method============")
runAgain = True
while runAgain:    
    for i in range(10, -1, -1):
        if i ==0:
            print(i, " BLASTOFF!!")
        else:
            print(i)
    while True: # validation while loop
        answerValue = input("Do you want to continue? (Y/N) ").upper()
        if answerValue in ["N","Y"]:
            if answerValue == "N":
                runAgain = False
            break # Exit the validation while loop
        else:
            print("Enter Y or N only, please")


