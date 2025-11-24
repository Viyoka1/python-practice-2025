# %%
42 == 44 
# %%
# Single variable
s = "Bob"
print(s)

# multiple variables
s = 'Alice'
age = 30
city = 'New York'
print(s, age, city)
# %%   
# split() method is used to split a string into a list where each word is a list item
# taking two inputs at once
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at once 
x, y, z = input("Enter three values: ").split()
print("Total nuumber of students: ", x)
print("Number of boys : ", y)
print("Number of girls: ", z)
# %%
# How to change the type of input
# by default input() functions helps in taking user input as string.add()
# Taking input as string 
color = input("What color is rose?: ")
print("Rose is ", color)

# %%
# Print integer value
n = int(input("How many roses do you want?: "))
print("Number of roses: ", n)
# %%
# float/decimal number
price = float(input("Enter the price of a dozen roses: "))
print("Price of a dozen rose is: ", price)
# %%
# counting characters in a string 
word = "Potato Bob"
length = len(word)
print("Length of the word is: ", length)

# %%
# Arthemetic operations
a = 500 
b = 22

# Addition 
print("Addition: ", a + b)
# Subtraction
print("Subtraction: ", a - b)
# Multiplication 
print("Multiplication: ", a * b)
# Division 
print("Division: ", a / b)
# Floor Division 
print("Floor Division: ", a // b)
# Modulus 
print("Modulus: ", a % b)
# Exponentiation
print("Exponentiation: ", a ** b)
# %%
# Comparison operators 
a = 15 
b = 20

print(a > b) # Greater than
print(a < b) # less than
print(a == b) # equal to 
print(a != b) # not equal to 
print(a >= b) # Greater than or equal to
print(a <= b) # less than or equal to 
# %%
# Logical operators
a = True
b = False

print(a and b) # Logical AND
print(a or b) # logival OR
print(not a) # Logical NOT
# %%
# Assignment operators
a = 15
b = a   

print(b)
b += a  # b = b + a
print(b)
b -= a  # b = b - a   
print(b)
b *= a  # b = b * a     
print(b)

# %%
# Membership operators
x = 13
y = 34 
list = [10, 13, 22, 45, 67]

if (x not in list):
    print("x is NOT present in the list")
else: 
    print("x is present in the list")

if (y in list):
    print("y is present in the list")
else: 
    print("y is NOT present in the list")

# %%
# Ternary operator
a , b = 15, 30 
min = a if a < b else b
print(min)
# %%
