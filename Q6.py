
#String Immutable
s = "Dog"
s[0]

s[0] = "R"

#Output is an Error: TypeError
#Solution: create copy and slice

#List mutable

lst = [1, 3, 5, 7, 8, 10]
print(lst[1])

lst[1] = 11
print(lst)
