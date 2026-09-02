# Exercise 1 - Neuron types

# Create a list containing three different neuron types. 
# Then print the entire list

neuron_types = ["sensory", "excitatory", "inhibitory"]

print(neuron_types) 

# Exercise 2 - Accesing neuron types

neuron_types = ["sensory", "excitatory", "inhibitory"]
print(neuron_types[0])
print(neuron_types[2])
print(f"Número de items: {len(neuron_types)}")

# Exercise 3 - Modifying neuron types

neuron_types = ["sensory", "excitatory", "inhibitory"]
neuron_types[2] = "motor" # MODIFICAMOS un elemento de la lista

print(neuron_types)
print(neuron_types[0])
print(neuron_types[2])
print(f"Número de items: {len(neuron_types)}")

# Exercise 4 - Adding neuron types 
# Now we are going to add something new: append()
# We want add one element whithout replace another

neuron_types = ["sensory", "excitatory", "inhibitory"]
neuron_types.append("motor") # Añadimos un elemento al FINAL de la lista
print(neuron_types)

# Exercise 5 - append() + len()
neuron_types = ["sensory", "excitatory", "inhibitory"]
neuron_types.append("motor")
neuron_types.append("interneuron")

print(neuron_types)
print(neuron_types[0])
print(neuron_types[-2]) # Forma de llamar al último elemento de la lista
print(f"Número de items: {len(neuron_types)}")

# Exercise 6 - List + 'for'
    #for item in list:      → Structure for iterations on lists
        #do_something(item) →
        
neuron_types = ["sensory", "excitatory", "inhibitory","motor","interneuron"]

for neuron_type in neuron_types:
    print(f'This kind of neuron is: {neuron_type}')

# Exercise 7 - List + 'for' + 'if'
# Now we are going to classify each kind of neuron 
    # For example → "sensory" → Sensory neuron : "excitatory" → Excitatory neuron
    
neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for neuron_type in neuron_types:
    if neuron_type == "sensory":
        print(f'{neuron_type} → Sensory neuron: The sensory neuron conducts impulses from the receptors (skin, eyes, etc.) to the central nervous system.')
    elif neuron_type == "excitatory":
        print(f'{neuron_type} → Excitatory neuron: The excitatory neuron increases the probability that the postsynaptic neuron will generate an action potential.')
    elif neuron_type == "inhibitory":
        print(f'{neuron_type} → Inhibitory neuron: It decreases the probability that the postsynaptic neuron will fire.')
    elif neuron_type == "motor":
        print(f'{neuron_type} → Motor neuron: It transmits commands from the CNS to muscles or glands to generate movement or secretion.')
    else:
        print(f'{neuron_type} → Interneuron neuron: It acts as a connecting bridge between other neurons within the CNS, responsible for integration and reflexes.')
        
# Exercise 8 - List + for + len()
# Classify and enumerate each type of neuron. Whitouth a description. 

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for index, neuron_type in enumerate(neuron_types):
    print(f'Neuron {index + 1}: {neuron_type}')

print(f'Total neurons: {len(neuron_types)}')

# Exercise 9 - Filtering neuron types
# We want to filter the list and print only the excitatory and inhibitory neurons.
# Restrictions: Use only 'for', 'if', 'elif', 'print()', and '=='

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for neuron in neuron_types:
    if neuron == "excitatory":
        print(neuron)
    elif neuron == "inhibitory":
        print(neuron)
    else:
        continue                # En python no es necesario aclarar que hacer con las condiciones que no se cumplen. 

# Exercise 10 - Simplify the code
 
neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for neuron_type in neuron_types:
    if neuron_type == "excitatory":
        print(neuron_type)
    elif neuron_type == "inhibitory":
        print(neuron_type)

# Exercise 11 - Using 'or'

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for neuron_type in neuron_types:
    if neuron_type == "excitatory" or neuron_type == "inhibitory":
        print(neuron_type)
        
# Exercise 12 - Filtering with multiple conditions
# Goal: Print the neuron types that are excitatory OR inhibitory OR motor.

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for neuron_type in neuron_types:
    if neuron_type == "excitatory" or neuron_type == "inhibitory" or neuron_type == "motor":
        print(neuron_type)

# Exercise 13 - The 'in' operator 
# We want the same last result but using the 'in' operator.

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for neuron_type in neuron_types:
    
    if neuron_type in ["excitatory","inhibitory","motor"]:
        print(neuron_type)


# Integration Challenge

# 14 - Classify and enumerate

# We want to show only the types of neurons that are active: excitatory, inhibitory and motor
# Each one of this neurons should be enumerated
# Output expected: "Neuron 1: excitatory ; Neuron 2: inhibitory"...

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

for index, neuron_type in enumerate(neuron_types):
    if neuron_type in ["excitatory","inhibitory","motor"]: # Acá vemos el problema de enumerar por el índice.
        print(f'Neuron {index}: {neuron_type}')            # Si el elemento estuviera en otro lado no sería un enumeramiento natural.
        
# Exercise 15 — Neuron classification

# We want to classify each neuron type into two groups → functional or not-functional
# For this exercise, we are going to classify as functional neurons → sensory and motor neurons. 
# And we will classify as non-functional neurons → excitatory, inhibitory and interneuron.
# Expected output: 
    # "sensory → functional
    # excitatory → not-functional", etc. 

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]
functional_neurons = ("sensory","motor")
non_functional_neurons = ("excitatory","inhibitory","interneuron")

for neuron_type in neuron_types: 
    if neuron_type in functional_neurons:
        print(f'{neuron_type} → functional')
    elif neuron_type in non_functional_neurons:
        print(f'{neuron_type} → non-functional')
    
# Exercise 16 - Counting neuron categories

# We have a little neuronal poblation
# We need to know how many "excitatory neurons" exists in this poblation of neurons.
# We need a counter
# Expected output: "Excitatory neurons: 3"
    
neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "excitatory", "inhibitory", "excitatory"]
counter = 0

for neuron_type in neuron_types:
    if neuron_type == "excitatory":
        counter += 1     
print(f'Excitatory neurons: {counter}')

# Exercise 17 - Checking neuron types
# We need to check whether our neuron population contains two specific neuron types: motor and interneuron.
# Expected output: "Motor neuron found" "Interneuron found"

neuron_types = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

if "motor" in neuron_types:
    print('Motor neuron found')
else:
    print('Motor neuron not found')

if "interneuron" in neuron_types:
    print('Interneuron found')
else:
    print('Interneuron not found')

# Exercise 18 - Simulating a Neural Population
# We have a little neural population: 
# We want to analyze only two types based on excitation and inhibition.

population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
counter = 0

for neuron_type in population: 
    if neuron_type == "excitatory":
        counter += 1
        print(neuron_type)
    elif neuron_type == "inhibitory":
        counter += 1
        print(neuron_type)        
print(f'Total: {counter}')

# Busquemos otra forma de hacerlo

population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
counter = 0

for neuron_type in population: 
    if neuron_type == "excitatory" or neuron_type == "inhibitory":
        counter += 1
        print(neuron_type)        
print(f'Total: {counter}')

# Busquemos otra forma de hacerlo → Esta vez con in

population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory"]
counter = 0

for neuron_type in population: 
    if neuron_type in ["excitatory","inhibitory"]:
        counter += 1
        print(neuron_type)
print(f'Total: {counter}')

# Exercise 19 - Mini Neural Population Analysis
# We have a growing population 

population = ["sensory","motor","interneuron","motor","excitatory","interneuron","excitatory","interneuron","inhibitory","motor","excitatory","interneuron","inhibitory","motor","excitatory","inhibitory","sensory","motor"]

# We need a program to analyze the population.
# Count how many neurons are in the population and classify them by type. 

# Counters
sensory_counter = 0
inhibitory_counter = 0
motor_counter = 0
excitatory_counter = 0
interneuron_counter = 0

for neuron_type in population:
    if neuron_type == "sensory":
        sensory_counter += 1
    elif neuron_type == "inhibitory":
        inhibitory_counter += 1
    elif neuron_type == "excitatory":
        excitatory_counter += 1
    elif neuron_type == "motor":
        motor_counter += 1
    else:
        interneuron_counter += 1
population_counter = len(population)

print(f'Sensory neurons: {sensory_counter}')
print(f'Inhibitory neurons: {inhibitory_counter}')
print(f'Excitatory neurons: {excitatory_counter}')
print(f'Motor neurons: {motor_counter}')
print(f'Interneurons: {interneuron_counter}')

print(f'Total neurons in population: {population_counter}')

# Exercise 20 - Experimental Neuron Population

# Now we are goingto introduce a new concept: input()
# Until now, we introduce data directly, but a interesting program should be to get information directly from the user.
# input() → Make it possible // input("Enter a neuron type: ") 

# Exercise 21 - Neuron Type Checker

# The program should contain a population and ask the user which type of neuron they want to search for.
# For example: "Enter a neuron type: motor"
# Then, check whether that neuron type is in the population.
# If it is not in the population, print "motor neuron not found".

population = ["sensory", "excitatory", "inhibitory", "motor", "interneuron"]

# to_find = input("Enter a neuron type: ")

#if to_find in population: 
#    print(f'{to_find} → found')
#else:
#    print(f'{to_find} → not found') 

# Exercise 22 - Neuron type counter

# We have a growing population: 
# The user needs to search for and count how many neurons of a specific type are in the population.
# Code ↓
 
#population = ["sensory","excitatory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory","sensory","motor","excitatory"]
#to_find = input("Enter a neuron type: ").lower()
#counter = 0
#
#for neuron_type in population: 
#    if to_find == neuron_type:
#        counter +=1 
#print(f'You have {counter} type of {to_find} neurons → ')
    
# Exercise 23 - Case-insensitive neuron search
# Modify the previous exercise so that the user can type any combination of lowercase and uppercase letters.
# For example: 'Enter a neuron type: iNhiBitorY'
# You have 2 inhibitory neurons → .
# Code ↑

# Exercise 24 - Neuron Frequency Classification

# Now our program needs to do something more similar to an analysis pipeline
# We have a population and the user enters a neuron type:
# You program should: 
    # Any input should be converted to lowercase
    # Count how many times this neuron type appears in the population.
    # Classify the frequency: 0 → absent; 1-2 → rare; 3+ → common
# Expected output: excitatory → 4 neurons → common

# Inputs
population = ["sensory","excitatory","sensory","excitatory","inhibitory","motor","excitatory","interneuron","inhibitory","sensory","motor","excitatory"]
to_find = input('Enter a neuron type: ').lower()

# Counters 
sensory_counter = 0
excitatory_counter = 0
inhibitory_counter = 0
interneuron_counter = 0
motor_counter = 0
others_counter = 0

# Classifier 

for neuron_type in population:
    if neuron_type == "sensory":
        sensory_counter += 1
    elif neuron_type == "excitatory":
        excitatory_counter += 1
    elif neuron_type == "inhibitory":
        inhibitory_counter += 1
    elif neuron_type == "interneuron":
        interneuron_counter += 1
    elif neuron_type == "motor":
        motor_counter += 1
    else:
        others_counter += 1

if to_find == "sensory":
    if sensory_counter == 0:
        print(f'You have {sensory_counter} of sensory neurons → absent')
    elif 1 <= sensory_counter <= 2:
        print(f'You have {sensory_counter} of sensory neurons → rare')
    else:
        print(f'You have {sensory_counter} of sensory neurons → common')
elif to_find == "excitatory":
    if excitatory_counter == 0:
        print(f'You have {excitatory_counter} of excitatory neurons → absent')
    elif 1 <= excitatory_counter <= 2:
        print(f'You have {excitatory_counter} of excitatory neurons → rare')
    else:
        print(f'You have {excitatory_counter} of excitatory neurons → common')
elif to_find == "inhibitory":
    if inhibitory_counter == 0:
        print(f'You have {inhibitory_counter} of inhibitory neurons → absent')
    elif 1 <= inhibitory_counter <= 2:
        print(f'You have {inhibitory_counter} of inhibitory neurons → rare')
    else:
        print(f'You have {inhibitory_counter} of inhibitory neurons → common')
elif to_find == "interneuron":
    if interneuron_counter == 0:
        print(f'You have {interneuron_counter} of interneuron neurons → absent')
    elif 1 <= interneuron_counter <= 2:
        print(f'You have {interneuron_counter} of interneuron neurons → rare')
    else:
        print(f'You have {interneuron_counter} of interneuron neurons → common')
elif to_find == "motor" :
    if motor_counter == 0:
        print(f'You have {motor_counter} of motor neurons → absent')
    elif 1 <= motor_counter <= 2:
        print(f'You have {motor_counter} of motor neurons → rare')
    else:
        print(f'You have {motor_counter} of motor neurons → common')
else: 
    if others_counter == 0:
        print(f'You have {others_counter} of {to_find} neurons → absent')
    elif 1 <= others_counter <= 2:
        print(f'You have {others_counter} of {to_find} neurons → rare')
    else:
        print(f'You have {others_counter} of {to_find} neurons → common')

# Luego de semejante monstruo condicional, toca aprender nuevas herramientas. 
