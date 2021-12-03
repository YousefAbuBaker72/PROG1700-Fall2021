sum=0 #Initializing the value of sum

for counter in range(10): # start value of counter is 0 . 
    # We have the default logical condition to keep performimng 
    # the loop(Keep interating) >>>> if counter <10
    # The counter value will be increased by 1
    sum=sum+counter
    print("counter= ",counter)
print("the total sum is : ",sum)

sum=0
counter=0
while counter<10:
    sum=sum+counter
    print("counter= ",counter)
    # counter = counter+1
    counter +=1
print("the total sum from While loop is : ",sum)

sum=0 #Initializing the value of sum
for counter in range(2,20,3): # start value of counter is 2 . 
    # We have the default logical condition to keep performimng 
    # the loop(Keep interating) >>>> if counter < 20
    # The counter value will be increased by 3 for each interation

    sum=sum+counter
    print("counter= ",counter)
print("the total sum is : ",sum)

sum=0 #Initializing the value of sum

for counter in range(20,2,-2): # start value of counter is 20 . 
    # We have the default logical condition to keep performimng 
    # the loop(Keep interating) >>>> if counter > 2
    # The counter value will be increased by 3 for each interation

    sum=sum+counter
    print("counter= ",counter)
print("the total sum is : ",sum)




