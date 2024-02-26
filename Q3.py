import datetime
a = 7
b = 2
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
#a = 7

print(b)
#b = 4

c = a + b
print(c)
#c=11

d = "xyz" * (c//3)
print(d)
#xyzxyzxyz