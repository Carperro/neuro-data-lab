# We will use the same methodology as in the previous file. 

# Excercise 1 - if/else statement
# We will use the if/else statement to check if a person is an adult or not

# 1 - Create a variable called age. 
# 2 - If age is 18 or greater, print "You are an adult" ; Otherwise, print "You are a minor"

age = 11

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Exercise 2 - if/elif/else statement
# We will use the if/elif/else statement to check whether a person is a child, teenager or adult. 
# Under 13 → Child ; Under 17 → Teenager ; 18 and over → Adult.

if age < 13:
    print ("You are a child") 
elif age <= 17:
    print ("You are a teenager")
else :
    print ("You are an adult")
    
# Comparison Operators

# Operator          Meaning                       Example

# ==                Equal to                     5 == 5 → True
# !=                Not equal to                 5 != 3 → True
# >                 Greater than                 5 > 3 → True    
# <                 Less than                    3 < 5 → True
# >=                Greater than or equal to     5 >= 5 → True
# <=                Less than or equal to        3 <= 5 → True

# Exercise 3 - Comparison operators

age = 20 

# Is age equal to 18? 
print(age == 18) #False
# Is age not equal to 18?
print(age != 18) #True
# Is age greater than 18?
print(age > 18) #True
# Is age less than 18?
print(age < 18) #False
# Is age greater than or equal to 18?
print(age >= 18) #True
# Is age less than or equal to 18? 
print(age <= 18) #False

result = age >= 18
print(result)
print(type(result)) 

# Exercise 4 - Logical operators
# We will use the and, or, and not operators to combine multiple conditions.

age = 20

# Is age between 18 and 30?
print(age >= 18 and age <=30) #True
# Is age under 18 or over 65?
print(age < 18 or age > 65) #False
# Is age not equal to 20?
print(age != 20) #False
# Is age greater than 18 and less than 25? 
print(age > 18 and age < 25) #True
# Comparison with not operator
print(not age == 20) #False age >= 18 and age <= 30 // 18 <= age <= 30 → Other style to write the same condition.

# Exercise 5 - Student performance → First integrator exercise of conditionals.
# Now we will move closer to a type of logic that we will use with real data.
# We want a program that evaluates student performance based on study hours.
# Less than 2 hours → Low study time ; 2 to 4 hours → Moderate study time ; More than 4 hours → High study time.
# Requirements: One variable called "study_hours"; if, elif, else statements; comparison operators. 

study_hours = 44

if study_hours < 2:
    print("Low study time")
elif study_hours >= 2 and study_hours <= 4:
    print("Moderate study time")
else:
    print("High study time")
    
# More concise version using a chained comparison.
 
study_hours = 4.6
is_student = True

if not is_student:
    print("Is not a student")
elif study_hours < 2:
    print("Low study time")
elif 2 <= study_hours <= 4:
    print ("Moderate study time")
else: 
    print("High study time")
    
###

is_student = True
age = 22
study_hours = 6
if not is_student:
    print("Not a student")
elif age < 18:
    print("Underage student")
elif study_hours < 2:
    print("Low study time")
elif 2 <= study_hours <= 4:
    print("Moderate study time")
else:
    print("High study time")
    
    