#Acadgild This code belong to Python 1 Problem Statement 2


first_divisor = 7
second_divisor = 5

range_lower_limit = 2000
range_upper_limit = 3200

list_to_print = []

for counter in range(range_lower_limit,range_upper_limit+1):
    if (counter%first_divisor == 0 and counter%second_divisor != 0):
         list_to_print.append(counter)

print(list_to_print)