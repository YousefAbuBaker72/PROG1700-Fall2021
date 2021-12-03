# Arrays ---- Lists
#Index value:
#           0        1        2       3 
stNames=["Yousef", "David", "Mary", "Sam"]
print(stNames)

print(stNames[0]) # First Element of the List
print(stNames[1]) # 2nd Element of the List
print(stNames[2]) # 3rd Element of the List
print(stNames[3]) # 4th Element of the List

for i in range(4):
    print(stNames[i])

stNames.append("Brad")
for i in range(len(stNames)):
    print(stNames[i])
stNames.sort()
print(stNames)
stNames.reverse()
print(stNames)
print(stNames.count("Yousef"))
stNames.insert(2, "New Name")
print(stNames)
stNames.remove("New Name")
print(stNames)


