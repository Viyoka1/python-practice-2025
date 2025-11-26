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
# program to convert a Fahrenheit temperature to Celsius temperature
inp = input("Enter tempperature in Fahrenheit: ")
fahrenheit = float(inp)
cel = (fahrenheit - 32) * 5.0/9.0
print(f"Temperature in Celsius is: {cel} C")

# %%
# Try and Except feature in Python act as an "insurance policy" on a sequence of statements
# temperature conversion with error handling 

inp = input("Enter temperature in Fahrenheit: ")
try: 
    fahrenheit = float(inp) 
    celcius = (fahrenheit - 32) * 5.0/9.0
    print(f"Temperature in Celsius is: {celcius:} C")
except: 
    print("Please enter a number")

# %%
# Conditional statement exercise
# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
employee_hours = input("Enter hours worked: ")
hours_worked = float(employee_hours)
employee_rate = 10.00 
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (employee_rate * 1.5)
    total_pay = (40 * employee_rate) + overtime_pay 
else: 
    total_pay = hours_worked * employee_rate

print(f"Your total pay for this cycle is: {total_pay}")
# %%
# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
score_input = input("Enter score between 0.0 to 1.0: ")
try: 
    score = float(score_input) 
    if score < 0.0 or score > 1.0: 
        print("Error: Score out of range")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else: 
        print("F")
except:
    print("Please enter a valid number")