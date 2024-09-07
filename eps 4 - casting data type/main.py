# casting is changing the data type to other data type

# int to other type
print("=====integer=======")

integer = 10
print ("before casting this type is", type(integer))

a = float(integer)
print (a, "after casting to float", type(a))
b = str(integer)
print (b, "after casting to string", type(b))
c = bool(integer)
print (c, "after casting to bool", type(c))


# float to other type
print("=====float========")
floatt = 9.9
print(floatt, "before casting is", type(floatt))

a = int(floatt)
print(a, "after casting to integer", type(a))
b = str(floatt)
print (b, "after casting to string", type(b))
c = bool(floatt)
print (c, "after casting to bool", type(c))


# boolean to other type
print("=====boolean========")
boolean = False
print(boolean, "before casting is", type(boolean))

a = int(boolean)  # -> if true integer will be 1 and if false will be 0
print(a, "after casting to integer", type(a))
b = str(boolean)
print (b, "after casting to string", type(b))
c = float(boolean)  # -> if true float will be 1.0 and if false will be 0.0
print (c, "after casting to bool", type(c))


# string to other type
print("=====string=======")

string = "1000"
print ("before casting this type is", type(string))

a = float(string)  #will eror if the string is not number
print (a, "after casting to float", type(a))
b = int(string) #will eror if the string is not number
print (b, "after casting to string", type(b))
c = bool(string) #will false if the string is empty ("")
print (c, "after casting to bool", type(c))