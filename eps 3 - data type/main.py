# data type : 
# a. integer ( 1 , 2 , 3 , etc) -> number
# b. float ( 1.1 , 1.2 , etc) -> decimal number
# c. string ("example 1" , "example 2" , etc) -> use "" 
# d. boolean ( true/false) -> if 0 is false and if not 0 is true
integer = 1
float = 1.2
string = " bisa ini bisa juga ini pake 1"
boolean = True

print (integer, "is", type(integer))
print (float, "is", type(float))
print (string, "is", type(string))
print(boolean, "is", type(boolean))

# example of boolean
# the answer will true true false

a = 1
b = -1
c = 0

boolean = bool(a), bool(b), bool(c)
print(boolean)


a = 1.5
b = int(a)
print(b, type(b))