# %%
# Numberica Data Types
a = 5 
print(type(a))
b = 5.0
print(type(b))
c = 5 + 3j
print(type(c))
# %%
# Sequence Data Types
# String 
s = 'Potato Bob'

# check data type
print(type(s))

# access string with index 
print(s[3])
print(s[2])
print(s[-1])
# %%
# list data type 
# empty list 
a = []

# list with int values 
a = [1, 3, 5, 7, 5]
print(a)

# list with mixed values int and string 
b = ["apple", "banana", 1, 3, 5]
print(b)
# %%
# acces list items 
a = ["Potato", "and", "Beans"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative index")
print(a[-1])
print(a[-3])

# %%
# Tuple data type 
# Tuple is an ordered collection of items which is immutable. Tuples cannot be modified once created.
# initialize empty tuple
t = ()

t2 = ('apple', 'banana', 1, 3, 5)
print("Tuple with mixed values: \n", t2)
# %%
# accessing tuple items 
t = tuple([1, 3, 5, 7, 9])

# accessing tuple items using index
print(t[0])
print(t[3])
print(t[-1])
# %%
# Create a set in python 
# initializing empty set 
s1 = set()

s1 = set("potatobob")
print("Set with the use of string: \n", s1)

s2 = set(["Patoto", "Bob"])
print("Set with the use of list: \n", s2)

# %%
# accesing set items 
set1 = set(["Potato", "Bob"])
print(set1)

# loop through the set items 
for i in set1:
    print(i, end=" ")  # prints element one by one

# check if item exist in the set 
print("Geeks" in set1)
# %%
# dictiionary data type 
# create a dictionary
d = {}
d = {1: "apple", 2: "banana", 3: "grape"}
print(d)
# creating dictionary using dict() constructor 
d1 = dict({1: "apple", 2: "banana", 3: "grape"})
print(d1)

# %%
d = {1: "apple", 2: "banana", 3: "grape"}

# accesiing an element using key 
print(d[1])
# accessing an element using get() method
print(d.get(2))
# %%
