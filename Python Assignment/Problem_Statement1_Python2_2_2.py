#Acadgild This code belong to Python 1 Problem Statement 2


max_number_stars = 5
#The above variable represents the maximum number of stars to be printed on a row

for row_number in range(0,max_number_stars):
    for counter_stars in range(0,row_number+1):
            print('* ', end=' ')
    print("\r")


for row_number in range(max_number_stars,0,-1):
    for counter_stars in range(0,row_number+1):
            print('* ', end=' ')
    print("\r")

