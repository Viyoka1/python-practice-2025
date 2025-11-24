# %% 
age = 20 
if age >= 18:
    print("You are eligible to vote")
# %%
age = 15
if age > 18: print("You are elgible to vote")
# %%
# if else conditional statement 
age = 15
if age <= 12:
    print("Eat for free")
else:
    print("Eat for $10")
# %%
# short hand if else 
Lily = 13
res = "Eligible to vote" if Lily >= 18 else "Not eligible to vote"
print(f"Result: {res}")

# %%
# elif statement 
age = 65

if age <= 12:
    print("Eat for free")
elif age <= 19: 
    print("Eat for $5")
elif age <= 59:     
    print("Eat for $10")
else: 
    print("eat for $7")

# %%
age = int(input("Enter your age: "))

# ask if the user is a member of the club
member_input = input("Are you a member of the club? (yes/no): ").strip().lower()
is_member = member_input == "yes"

# check for discount eligibility
if age >= 65 and is_member:
    if is_member: 
        print("30% senior discount")
    elif age >= 65:
        print("20% senior discount")
else:
    print("Not eligible for senior discount!")
# %%
# movie ticket price based on age
age = int(input("Enter your age: "))

if age < 12:
    print = 8
elif age <= 64:
    price = 12
else: 
    price = 6
print(f"Your ticket price is: ${price}")
# %%
# Number Guessing Game 
import random 
number_to_guess = random.randint(1,10)
user_guess = 0

while user_guess != number_to_guess: 
    user_guess = int(input("Guess a number between 1 and 10: "))
if user_guess < number_to_guess: 
    print("Too Low! Try again.")
elif user_guess > number_to_guess: 
    print("Too High! Try again.")
else: 
    print("Congratulations! You guessed it right.")

# %%
# Simple login system 
username = input("Enter your username: ")
password = input("Enter your password: ") 

if username == "admin" and password == "password123": 
    print("Login successful!")
else: 
    print("Invalid username or password.") 
# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%

# %%
