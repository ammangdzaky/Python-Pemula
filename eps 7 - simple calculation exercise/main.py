# -------SIMPLE TEMPERATURE CONVERTER

# CELCIUS TO OTHER TEMPERATURE UNITS

celsius = float(input("masukkan suhu dalam celsius: "))
print("suhu bernilai", celsius,  "C")

r = (4/5) * celsius
print("dalam reamur bernilai = ", r, "R")

f = (9/5) * celsius + 32
print("dalam fahrenheit bernilai = ", f, "F")

k = celsius + 273
print("dalam kelvin bernilai = ", k, "K")


# reamur TO OTHER TEMPERATURE UNITS
print("=======================================")

reamur = float(input("masukkan suhu dalam reamur: "))
print("suhu bernilai", reamur,  "R")

c = (5/4) * reamur
print("dalam celsius bernilai = ", c, "C")

f = (9/4) * reamur + 32
print("dalam fahrenheit bernilai = ", f, "F")

k = (5/4) * reamur + 273
print("dalam kelvin bernilai = ", k, "K")

# fahrenheit TO OTHER TEMPERATURE UNITS
print("=======================================")

fahrenheit = float(input("masukkan suhu dalam fahrenheit: "))
print("suhu bernilai", fahrenheit,  "F")

c = 5/9 * (fahrenheit - 32)
print("dalam celsius bernilai = ", c, "C")

r = 4/9 * (fahrenheit - 32)
print("dalam reamur bernilai = ", r, "R")

k = c + 273
print("dalam kelvin bernilai = ", k, "K")


# kelvin TO OTHER TEMPERATURE UNITS
print("=======================================")

kelvin = float(input("masukkan suhu dalam kelvin: "))
print("suhu bernilai", kelvin,  "K")

c = kelvin - 273
print("dalam celsius bernilai", c, "C")

r = (4/5) * kelvin - 273
print("dalam reamur bernilai", r, "R")

f = (9/5) * c + 32
print("dalam fahrenheit bernilai", f, "F")




