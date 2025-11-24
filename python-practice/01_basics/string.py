# %%
len("Hello, World!")  # 13
# %%
# Concatenation - joining two strings
# Indexing - accessing individual characters
# Slicing - extracting a substring
string1 = "Potato"
string2 = "Tomato"
combined = string1 + string2
print(combined)

# %%
first_name  = "Austin"
last_name = "Niu" 
full_name = first_name + " " + last_name
print(full_name)
# %%
# Indexing - accessing individual characters
dessert = "Ice Cream" 
dessert[3]

# %%
user_input = "Python"
final_index = len(user_input) - 1 
final_index
last_chracter = user_input[final_index]
print(last_chracter)
# %%
# slicing - extracting a substring
language = "JavaScript" 
substring = language[0:4]
print(substring)

# %%
dessert = "Matcha Ice Cream"
substring = dessert[-7:]
# %%
# Omitting start or end index
fruit = "Watermelon"
substring1 = fruit[:5]
substring2 = fruit[5:]
print(substring1)
print(substring2)
# %%
word = "boil"
word = "f" + word[1:]
print(word)
# %%
# Create a string and print its length using len()
string1 = "Potatobob"
length_of_string1 = len(string1)
print(length_of_string1)
# %%
# Create two strings, concatenate them, and print the resulting string
string1 = "Pineapple"
string2 = "Pizza"
combined_string = string1 + " " + string2 
print(combined_string)
# %%
# Print string "zing" by slicing the string "amazing"
word = "amazing" 
substring = word[3:]
print(substring)
# %%
# manipulate strings with methods
# converting String Cases, .lower(), upper(), .title()
name1 = "Viyoka Lim".lower()
name2 = "austin niu".upper()
string3 = "Love story".title()

print(name1)
print(name2)
print(string3)

# %%
name1 = " Viyoka Lim "
name2 = " austin niu "
name1.lower().strip()
name2.upper().strip()

print(name1.lower())
print(name2.upper())
# %%
# .rstrip() - removing whitespace from the right side of the string
# .lstrip() - removing whitespace from the left side of the string  
# .strip() - removing whitespace from both left and right with .strip() 
paragraph = "   Today have been a greaty day! I worked out and ate dinner     with my family.    "

cleaned_paragraph_1 = paragraph.lstrip()
cleaned_paragraph_2 = paragraph.rstrip()
cleaned_paragraph_3 = paragraph.strip()

print(cleaned_paragraph_1)
print(cleaned_paragraph_2)
print(cleaned_paragraph_3)
# %%
# startwith(0 and endwith()
# startswith() - checks if a string starts with a specified substring
# endswith() - checks if a string ends with a specified substring   
starship1 = "Enterprise"
starship2 = "Millennium Falcon"

start = starship1.startswith("En")
end = starship2.endswith("Falcon")

print(start)
print(end)
# %%
# Interact with user input and string methods 
prompt = input("What are three things you are grateful for today?")
graditude_list = prompt.split(",")
for item in graditude_list:
    print(item.strip().title())
    
# %%
prompt = input("What is your favorite ice cream?")
favorite_ice_cream = prompt.strip().lower()
print("Your favorite ice cream is:", favorite_ice_cream)

# %%
# Display the length of a user-inputted string
user_input = input("Enter your words of the day: ")
length_of_words = len(user_input)
print("The length of your word is: ", length_of_words)
# %%
num = "25"
num
# %%
num_pancakes = "5"
num_pancakes = str(int(num_pancakes) +2)
print(num_pancakes)
# %%
# Figure out how many pancakes left after eating some 
total_pancakes =input("How many pancakes did you made?")
pancaks_eaten = input("How many pancakes did you eat?")
pancakes_left = int(total_pancakes) - int(pancaks_eaten)
print("You have ", str(pancakes_left), "pancakkes left!")
# %%
# String concatenation with user input 

# %%
day = "Tuesday"
eggs = 3
bacon = 2
f"{day}'s breakfast I have {eggs} eggs and {bacon} strips of bacon."
# %%
# Create a float object named weight with the value 0.2, and create a string object named anaima with value "newt"
# Then use these objects to print the following string using only string concatenation
weight = 0.2 
animal = "newt"
f"{weight} kg is the weight of the {animal}."
# %%
# find a string or number in a sentence 
user_input = input("Enter a sentence: ")
search_term = input("Enter a word to search for: ")

# Conver both to strings (in case of number input)
user_input = str(user_input)
search_term = str(search_term)

# Make it case-insensitive 
found_index = user_input.lower().find(search_term.lower())

if found_index != -1:
    print(f"The term '{search_term}' was found at index {found_index}.")
else:
    print(f"The term '{search_term}' was not found in the sentence.")
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

# %%
