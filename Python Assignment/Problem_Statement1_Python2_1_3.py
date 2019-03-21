#Acadgild This code belong to Python 1 Problem Statement 2


firstName = input("Please enter the first name of the person ? ")
lastName = input("Please enter the last name of the person ? ")

separator = " "

print("The name of the person entered is \n")
print(firstName+separator+lastName)

print("We shall now print this in reverse order \n")
print(lastName[::-1]+separator+firstName[::-1])

