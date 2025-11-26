# %% 
# Function call
type(32)
# %%
# Math function
# Dot notation - format : object.function()
import math 
signal_power = 10.0
noise_power = 4.0
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
# %%
# Random number 
# Pusedo-random numbers are not truly random
import random 

for i in range(12): 
    x = random.random()
    print(x)
# %%
random.randint(5, 10)
# %%
random.randint(5,10)
# %%
# To choose an element from a sequence at random, you can use choice()
t = [1, 2, 3, 4, 5]
random.choice(t)
# %%
# Adding new functions 
# def is keyword to define a function definition
# empty parentheses means no input arguments
def print_lyrics():
    print("I'm a Lmberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()
# %%
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

# %%
# Parameter and arguments
def print_twice(bruce):
    print(bruce)
    print(bruce)
    
# %%
print_twice("Spam")
# %%
# Use any kind of expression as an argument for print_twice 
print_twice('Spam'* 4)

# %%
# Use a variable as an argument 
micheal = "Eric, the half a bee."
print_twice(micheal)
# %%
# Fruitful functions and void functions 
def addtwo(a, b):
    added = a + b
    return added 
x = addtwo(3, 5)
print(x)
# %%

# %%

# %%

# %%

# %%

# %%

# %%
