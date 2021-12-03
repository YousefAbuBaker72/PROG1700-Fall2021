#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #1. Welcome msg
    print("Welcome to the String Manipulator Program!")

    #2. Ask user to enter a word or phrase
    #print("I'm a regular string".upper())
    thePhrase = input("Please enter a word or phrase: ")    #.upper()

    #print(thePhrase).upper()   <-- This won't work!

    # #3. Display the unaltered phrase to user
    print("Unaltered Version: " + thePhrase)

    # #4. Display the all-upper version of the phrase
    print("Upper version: " + thePhrase.upper())

    # #5. Display the all-lower version of the phrase
    print("Lower version: " + thePhrase.lower())

    #6. Count and display the number of lower O's
    print("Count of O's: " , thePhrase.count("o"))

    #7. Determine and show if phrase is alphanumeric
    print("Is it numeric? " + str(thePhrase.isalnum()))

    #8. Changes S's to Z's and show altered phrase  #replace()
    #Original version (doesn't account for uppercase O)
    #print(thePhrase.replace("s", "z"))

    #Alternate method, using multiple replaces
    # firstPhrase = thePhrase.replace("s", "z")
    # secondPhrase = firstPhrase.replace("S","z")
    # print(secondPhrase)

    #Second alternate method - using command chaining
    print(thePhrase.replace("s", "z").replace("S", "z"))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()