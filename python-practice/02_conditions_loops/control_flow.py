# %% 
water_level = 50 
if water_level > 80: 
    print("Drain water") 
else: 
    print("continue filling")

# %%
print("Welcome to the roller coaster!")
user_input = int(input("Enter your height in cm: "))
height = user_input
if height >= 120:
    print("You can ride the roller coaster!")
else: 
    print("Sorry, you did not meet the height requirement.")
# %%
# Modulo operator 
# Check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else: 
    print(f"{number} is an odd number.")
# %%
# Nested if statements and elif statements 
# roller coaster with age-based pricing 
print("Welcome to Unicorn World!")
height = int(input("Enter your height in cm: "))
if height >=120: 
    print("You can ride the roller coaster!")
    age = input("Enter your age: ")
    age = int(age)
    if age <= 18: 
        print("Your ticket price is $7.")
    elif age > 18:
        print("Your ticket price is $12.")
else: 
    print("Sorry, you did not meet the height requirement.")
# %%
weight = float(input("Enter your weight in lbs: "))
height = float(input("Enter your height in inches: "))
# convert to metric 
weight = weight * 0.45
height = height * 0.025

bmi = weight / (height ** 2)
if bmi >= 25:
    print("You are overweight.")
elif bmi >= 18.5:
    print("You are normal weight.") 
else:
    print("You are underweight.")

# %%
# Theme park ticket package with add-ons photo 
print("Welcome to Unicorn Theme Park!")
height = int(input("Enter your height in cm: "))
if height >= 120: 
    print("You can ride the roller coaster!")
elif age > 12: 
    wants_photo = input("Do you want to purchase a photo? (Yes/No): ")
    if wants_photo.lower() == "yes":
        print("Photo added to your package. It costs an additional $3. Your total is $8.")
    else: 
        print("The total is $5.")
elif age <= 12: 
    wants_photo = input("Do you want to purchase a photo? (Yes/No): ")
    if wants_photo.lower() == "yes":
        print("Photo added to your package. It costs an additional $3. Your total is $13")
    else:
        print("The total is $10.")
elif age <= 18: 
    wants_photo = input("Do you want to purchase a photo? (Yes/No): ")
    if wants_photo.lower() == "yes": 
        print("Photo added to your package. It cost an additional $3. Your total is $16.")
    else: 
        print("Your total is $13.")

else: 
    print("Sorry, you do not meet the height requirement.")
# %%
print("Welcome to Unicorn Theme Park!")
height = int(input("Enter your height in cm: "))
if height >= 120: 
    print("You can ride the roller coaster!")
    age = int(input("Enter your age: "))
    if age < 12: 
        ticket_price = 5
    elif age <= 18:
        ticket_price = 10
    else: 
        ticket_price = 15 

    wants_photo = input("Do you want to purchase a photo? (Yes/No): ")
    if wants_photo.lower() == "yes":
            ticket_price += 3
            print(f"You total ticket price is: ${ticket_price}")
    else: 
            print(f"Your total ticket price is: ${ticket_price}")
else: 
    print("Sorry, You do not meet the height requirement.")
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

