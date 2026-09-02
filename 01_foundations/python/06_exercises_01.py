# Exercise 0 → def()
# Say hello and goodbye to a new researcher 

#name = input("What is your name? ")

#def say_hello():
#    print(f'Hello, {name}!')

#def say_goodbye():
#    print(f'Goodbye {name}!')

#say_hello()
#say_goodbye()

# Exercise 0.1 → def()
# Say hello and goodbye to a new researcher 
# Now using a parameter

#name = input("What is your name? ")

#def say_hello(name):
#    print(f'Hello, {name}!')  
#      
#def say_goodbye(name):
#    print(f'Goodbye, {name}!')
#
#name = input("Tell me your name: ")
#    
#say_hello("Pedro")
#say_hello("Lucas")
#say_goodbye(name)

# Exercise 0.2 - Only parameters
# Create one function that receives two parameters: neuron_type and signal
# The function should display something like: excitatory neuron → signal strength: 80 → inhibitory neuron → signal strength: 30

# Signal strength

#def calculator_strength(neuron_type,signal):
#    if neuron_type == "excitatory" and signal == 80:
#        print(f'Excitatory neuron → signal strength: {signal}')
#    elif neuron_type == "inhibitory" and signal == 30:
#        print(f'Inhibitory neuron → signal strength: {signal}')
#    else:
#        print('Incorrect parameters')
#
#calculator_strength("excitatory",80)

# Exercise 1 - First function → def()

# We have a population of neurons
# We need to create a function called → count_neurons()
# This function should: 
    # Receive a neuron type
    # Iterate through the population of neurons
    # Count how many times 'neuron_type' appears in the population
    # Print the results:
    # Output expected: excitatory → 3 neurons ; inhibitory → 2 neurons, etc
# New concept:
    # This time we add only def() and parameters.

# Data:     
#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]

#def count_neurons(neuron_type):
#    counter = 0
#    for neuron in population:
#        if neuron == neuron_type:
#            counter += 1
#    print(f"The neuron type '{neuron_type}' appears → {counter} times.")
#count_neurons("inhibitory")

# Exercise 2 - Function + Frequency Classification

# Create a function called 'count_neurons(neuron_type)'
# The function should:
    # Receive a neuron_type as parameter.
    # Iterate through the population
    # Count how many times that neuron type appears.
    # Classify its frequency: 0 → absent ; 1-2 → rare; 3+ → common.
    # Print the final result
# Expected output: 
    # If we execute: count_neurons("excitatory")
    # The neuron type 'excitatory' appears 3 times → common
    # The neuron type 'astrocyte' appears 0 times → absent 

#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
#
#def count_neurons(neuron_type):
#    counter = 0
#    for neuron in population:
#        if neuron == neuron_type:
#            counter += 1
#    
#    # Classification
#    if counter == 0:
#        frequency = "absent"
#    elif counter <= 2:
#        frequency = "rare"
#    else:
#        frequency = "common"                
#    print(f"The neuron type '{neuron_type}' appears {counter} times → {frequency}")            
#
#count_neurons("inhibitory")

# Exercise 3 - User input + function
# We want the user to choose which neuron type to analyze.

# The program should:
# 1. Ask the user to enter a neuron type.
# 2. Convert the input to lowercase.
# 3. Pass the selected neuron type to count_neurons().
# 4. Count how many times it appears in the population.
# 5. Classify its frequency:
#       0 → absent
#       1-2 → rare
#       3+ → common
# 6. Print the final result.

# Example:
# Enter a neuron type: EXCITATORY
# The neuron type 'excitatory' appears 3 times → common

#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
#chosen_neuron = input('Enter a neuron type: ').lower()
#
#def count_neurons(chosen_neuron):
#    counter = 0
#    for neuron in population:
#        if neuron == chosen_neuron:
#            counter += 1
#    # Classification
#    if counter == 0:
#        frequency = "absent"
#    elif counter <= 2:
#        frequency = "rare"
#    else:
#        frequency = "common"                
#    print(f"The neuron type '{chosen_neuron}' appears {counter} times → {frequency}")            
#
#count_neurons(chosen_neuron)

# Exercise 4 - return() vs print()

# Goal: Create a function called → count_neurons(neuron_type)
# The function should: 
    # 1 - Receive a neuron_type
    # 2 - Iterate through population
    # 3 - Count how many times that neuron appears
    # 4 - Return the counter
    # 5 - Outside the function, print the result
# Example: If we call → count = count_neurons("excitatory")
    # count should contain: 3 → then: print(count) → Should display: 3

#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
#neuron_type = input('Enter a neuron type: ').lower()
#
#def count_neurons(neuron_type): 
#    counter = 0
#    for neuron in population:
#        if neuron == neuron_type:
#            counter += 1            
#    return counter    # return hace que una función entregue un valor al lugar donde fue llamada.
#total = count_neurons(neuron_type)
#print(total)

# Exercise 5 - Returning the analysis → Neuron Population Analysis

# We have a neuron population.
# The user chooses a neuron type.
# Create a function called count_neurons().
# The function should:
# 1. Receive a neuron type as a parameter.
# 2. Iterate through the population.
# 3. Count how many times the neuron type appears.
# 4. Return the final count.
# Outside the function:
# 5. Store the returned value in a variable called total.
# 6. Classify the neuron type based on total:
#       0 → absent
#       1-2 → rare
#       3+ → common
# 7. Print the result.
# Example:
# Enter a neuron type: EXCITATORY
# The neuron type 'excitatory' appears 3 times → common

#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
#chosen_neuron = input('Enter a neuron type: ').lower()

#def count_neurons(chosen_neuron):
#    counter = 0
#    for neuron_type in population:
#        if neuron_type == chosen_neuron: 
#            counter += 1
#    return counter
#
#total = count_neurons(chosen_neuron)
#
#if total == 0:
#    print(f"The neuron type '{chosen_neuron}' appears {total} times → absent")
#elif total <= 2:
#    print(f"The neuron type '{chosen_neuron}' appears {total} times → rare")
#else: 
#    print(f"The neuron type '{chosen_neuron}' appears {total} times → common")

# Exercise 6 - Returning multiple values
# We have a neuron population.
# The user chooses a neuron type.
# Create a function called count_neurons().
# The function should:
# 1. Receive a neuron type as a parameter.
# 2. Iterate through the population.
# 3. Count how many times the neuron type appears.
# 4. Classify the frequency:
#       0 → absent
#       1-2 → rare
#       3+ → common
# 5. Return both the counter and the frequency.
# Outside the function:
# 6. Store the returned values in two variables.
# 7. Print the final result.
# Expected output:
# The neuron type 'excitatory' appears 3 times → common

#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]    
#chosen_neuron = input('Enter a neuron type: ').lower()
#
#def count_neurons(chosen_neuron):
#    counter = 0
#    for neuron_type in population:
#        if neuron_type == chosen_neuron:
#            counter += 1
#    # Classifier
#    if counter == 0:
#        frequency = "absent"
#    elif counter <= 2:
#        frequency = "rare"
#    else:
#        frequency = "common"
#    return counter, frequency
#
#total,frequency = count_neurons(chosen_neuron) 
#print(total)
#print(frequency)

# Exercise 7 - Two Parameters + Validation
# We have a neuron type and a signal strength.
# The user introduces both values.
# Create a function called analyze_neuron().
# The function should:
# 1. Receive two parameters:
#       neuron_type
#       signal_strength
# 2. Check the neuron type:
#       "excitatory" → valid
#       "inhibitory" → valid
#       anything else → invalid
# 3. If the neuron type is valid:
#       Display the neuron type and its signal strength.
# 4. If the neuron type is invalid:
#       Display an error message.
# Outside the function:
# 5. Ask the user for a neuron type.
# 6. Ask the user for a signal strength.
# 7. Pass both values to analyze_neuron().

# Expected output:
# Enter a neuron type: excitatory
# Enter signal strength: 80
# Excitatory neuron → signal strength: 80

# Another possible output:
# Enter a neuron type: motor
# Enter signal strength: 90
# Invalid neuron type
#neuron_type = input('Enter a neuron type: ').lower()
#signal_strength = input('Enter a signal strength: ')
#def analyze_neuron(neuron_type, signal_strength):
#    if neuron_type == "inhibitory" or neuron_type == "excitatory":
#        print(f'Neuron {neuron_type} → {signal_strength}')
#    else: 
#        print('Invalid parameters')
#analyze_neuron(neuron_type,signal_strength)
    
# Exercise 8 - Returning a classification

# The user enters a neuron type and its signal strength.
# Create a function called classify_signal().
# The function should:
# 1. Receive two parameters: neuron_type; signal_strength;
# 2. If the neuron is "excitatory":signal >= 70 → "strong"; signal < 70  → "weak"
# 3. If the neuron is "inhibitory": signal >= 40 → "strong" ;signal < 40  → "weak"
# 4. Any other neuron type: "unknown"
# 5. Return the classification.
# Outside the function:
# 6. Ask the user for the neuron type.
# 7. Ask the user for the signal strength.
# 8. Call the function with both values.
# 9. Store the returned classification in a variable.
# 10. Print the final result.
# Expected output:
# Enter a neuron type: excitatory
# Enter a signal strength: 80
# Neuron excitatory → strong

neuron_type = input('Enter a neuron type: ').lower()
signal_strength = int(input('Enter a signal strength: '))

def classify_signal(neuron_type, signal_strength):
    if neuron_type == "excitatory":
        if signal_strength >= 70:
            return "strong"
        else:
            return "weak"
    elif neuron_type == "inhibitory":
        if signal_strength >= 40:
            return "strong"
        else:
            return "weak"
    else: 
        return "Unknown"
    
# Guardo el resultado de la función en una variable
classification = classify_signal(neuron_type,signal_strength)   
                   
print(f"Neuron {neuron_type} → {classification}")

neuron_types = ["excitatory","inhibitory","sensory","motor","interneuron"]

for neuron in neuron_types:
    if neuron == "excitatory":
        print(neuron)
    elif neuron == "inhibitory":
        print(neuron)

