#Acadgild This code belong to Python 1 Problem Statement 2
from functools import reduce

max_find = lambda a,b: a if (a > b) else b

lst = [47,11,42,13]

reduce(max_find,lst)


