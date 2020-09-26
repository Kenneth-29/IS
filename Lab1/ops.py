#Kenneth Mogopodi CSE18-039

#Var decelerations
a = 23
b = 12
c = 2.402
name = "Kenneth"
Surname = "Mogopodi"

#Basic ops
full_name = name + " " + Surname        # Kenneth Mogopodi
sum = a + b                             # sum holds 35
product = a*b                           # product holds 276
sumth = a**b                            # sumth holds 21914624432020321
bb = b**2                               #  bb holds 144
divc = a/b                              # divc holds 1.9166666666666667
subtrct = a - b                         # subtrct holds 11
divs = a%b                              # divs holds 1.9166666666666667

# Assignment Ops
c += b                          # c is 14.402
d = e = f = g = h = i = 5       # d is 5
d -= 12                         # d is -7
e *= 0.5                        # e is 2.5
f /= 2                          # f is 2.5
g **= 2                         # g is 25
h %= 3                          # h is 2
i //= d                         # i is -1


# Comparison Ops
print(a == b)       # False
print(b != d)       # True
print(a < c)        # False
print(i > d)        # False
print(a <= 9)       # False
print(b >= b)       # False

# Logical Ops
print(True and True)
print(True or False)
print(True and False)
print(True and not False)

# a = true, b = false
print(True and False)       # False
print(True or False)        # True
print(True and not False)   # True

# a = false, b = true
print(False and True)       # False
print(False or True)        # True
print(False and not True)   # False

# a = False, b = False
print(False and False)      # False
print(False or False)       # False
print(False and not False)  # False


#String Ops
var1, var2, var3 = "Kenneth", "Mogopodi", "I love Python"
print(var1 + " " + var2)        # Kenneth Mogopodi
print(var3*2)                   # I love PythonI love Python
print(var3[:6] + " " + var1)    # I love Kenneth
print(var2 + " " + var3[2:])    # Mogopodi love Python
print("lov" in var3)            # True
print("lov" in var2)            # False
print("lov" not in var3)        # False
print("lov" not in var2)        # True

# Area of a circle
var4 = input("Enter the value of r (r being Radius):")
carea = 3.142 * int(var4) * 2
print("Area of the Circle is : %d" %(carea))

# Simple Interest calculation
rate, principal_amount, time = 0.03, 28000, 6
si = principal_amount*rate*time
print("The Simple interest of %d for %d years at %d percent, is %.2f"% (principal_amount, time, (100*rate),si))

# Control Structures
x = 21
if (x%2)==0:
    print("The number is odd")
else:
    print("The number is odd")

# Grades, A is above 80, B is 60-80, C is 50 to 60, and below 50 is D
y = 68
if(y<50):
    print("Your grade is D")
elif(y<60):
    print("Your grade is C")
elif(y<80):
    print("Your grade is B")
else:
    print("Your grade is A")

#while loop
z = 0
while(z<3):
    z += 1
    print("Python is Fun")

# range in python
q = range(1,10)
print(q[:3])
sum = 0
for a in q:
    print(a)

# calculating the sum in range
for a in q:
    sum = sum + a
print(sum)

# calculating the product of a range
prdct = 1
for a in q:
    prdct = prdct * a
print(prdct)