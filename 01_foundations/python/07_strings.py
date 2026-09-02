# Exercise 1 - Inspecting a string
# We have "neuron_name = 'hippocampus'"
# We need to obtain and print the first character of that string

#neuron_name = "hippocampus" 
#print(neuron_name[0]) # → First Character → indexing
#print(neuron_name[-1]) # → Last Character → negative index

# Exercise 2 - Slicing 
#neuron_name = "hippocampus" 
#print(neuron_name[0:5]) # → First five [start:end] 
#print(neuron_name[5:9]) # → Only print 'camp'

# Exercise 3 - len()
#print(len(neuron_name)) # Obtaining the length that an element contain

# Exercise 4 - Combining len() + indexing
#neuron_name = "hippocampus" 
#print(neuron_name[len(neuron_name)-1]) # → obtaining the last element, calculating its length as the index

# Exercise 5 - Concatenation 
#neuron_name = "hippocampus"
#neuron_type = "excitatory"
#print("The " + neuron_name + " neuron is " + neuron_type) # → Concatenation 
#print(f"The {neuron_name} neuron is {neuron_type}") # → Using f-string to simplify the process

# Exercise 6 - String methods
#neuron_type = "EXCITATORY" 
#print(neuron_type.lower())

# Exercise 7 - .strip()
#neuron_name = "   hippocampus   " # We have innecesaries spaces in the string, we need to remove thats 
#print(neuron_name.strip()) # → Remueve los espacios vacíos de los extremos

# Exercise 8 - .replace()
#neuron_name = "hippocampus" # We want changes all 'p' for 'x' → Expected = hixxocamxus
#print(neuron_name.replace('p','x')) # → Primero le damos como argumento lo que queremos remplazar, y luego el que irá en su lugar

# Exercise 9 - upper() + replace()
# We have: neuron_name = "hippocampus"
# We need: HIXO CAMPUS 
#neuron_name = ("hippocampus").upper().replace('P','X')
#print(neuron_name)

# Exercise 10 - strip() and upper()
#neuron_name = "   hippocampus   "
#print(neuron_name.strip().upper())

# Exercise 11 - replace() and lower()
# We have "EXCITATORY NEURON" → we wants "excitatory neuron"
#neuron_name = "EXCITATORY NEURON"
#print(neuron_name.lower().replace('neuron','cell'))

# Exercise 12 - split() 
#neuron_types = "excitatory inhibitory sensory motor" 
#print(type(neuron_types.split())) # → Acá utiliza como parámetro general el whitespace para separar

# Excercise 13 - split() with arguments
#neuron_data = "excitatory,inhibitory,sensory,motor"
#print(neuron_data.split(',')) # → Acá utiliza como parámetro general la (,) para separar los elementos

# Exercise 14 - split() + for
# We needs to print each type of neuron in a different line.
#neuron_data = "excitatory,inhibitory,sensory,motor"
#neuron_list = neuron_data.split(',')
#for neuron in neuron_list:
#    neuron.split()
#    print(f'Neuron: {neuron}')
    
# Exercise 15 - Mini Neuron Parser
# Expected output: 
    # Neuron 1: excitatory 
    # Neuron 2: inhibitory 
    # Neuron 3: sensory 
    # Neuron 4: motor 
    
#neuron_data = " EXCITATORY, inhibitory , SENSORY, motor " 
#neuron_list = neuron_data.lower().strip().split(',')
#for index, neuron in enumerate(neuron_list):
#    print(f'Neuron {index + 1}: {neuron.strip()}')
    
# Exercise 16 - Neural Data Cleaning
#Create a program that:
#Convert neural_data into a list using split().
#Loop through the list using for.
#Clean each neuron using strip() and lower().
#If the neuron is "unknown", skip it using continue.
#Use a counter to number only the valid neurons.
#Print each valid neuron using an f-string.     

#neural_data = " EXCITATORY, inhibitory, SENSORY, unknown, motor, INHIBITORY "
#neurons_list = neural_data.split(',')
#counter = 0
#for neuron in neurons_list:
#    if neuron.lower().strip() == "unknown":
#        continue    
#    counter += 1
#    print(f'{counter}: {neuron.lower().strip()}')
        
# Exercise 17 - String Search
# Create a program that:
# Convert neuron_data into a list.
# Loop through the list.
# Check if the neuron type is "inhibitory".
# Print only the inhibitory neurons.
 
#neuron_data = "excitatory, inhibitory, sensory, motor, inhibitory"
#neuron_list = neuron_data.split(',')
#for neuron in neuron_list: 
#    if "inhibitory" in neuron:
#        print(neuron.strip())

# Exercise 18 - Finding Information
# Create a program that:
# Convert neural_data into a list.
# Loop through the list.
# Clean each neuron using strip().
# Check whether the neuron is "inhibitory".
# Count how many inhibitory neurons there are.
# Print the final count.
# Expected output → Number of inhibitory neurons: 2

#neural_data = "excitatory, inhibitory, sensory, motor, inhibitory"
#neuron_list = neural_data.split(',')
#counter = 0
#for neuron in neuron_list:
#    if "inhibitory" == neuron.strip():
#        counter += 1
#print(f'Number of inhibitory neurons: {counter}')

# Exercise 19 - Neuron Type Counter

# Create a program that:
# Convert neural_data into a list.
# Loop through the list.
# Clean each neuron using strip().
# Count how many "excitatory" neurons there are.
# Count how many "inhibitory" neurons there are.
# Print both results.

#neural_data = "excitatory, inhibitory, sensory, motor, inhibitory, sensory, excitatory,excitatory, excitatory"
#neural_list = neural_data.split(',')
#excitatory_counter = 0 
#inhibitory_counter = 0 
#for neuron in neural_list:
#    if "excitatory" == neuron.strip():
#        excitatory_counter += 1
#    elif "inhibitory" == neuron.strip():
#        inhibitory_counter += 1 
#print(f'Excitatory neurons: {excitatory_counter}')        
#print(f'Inhibitory neurons: {inhibitory_counter}')        

# Exercise 20 - Unique Neuron Types
# Create a program that:
# Convert neural_data into a list.
# Loop through the list.
# Clean each neuron using strip().
# Store each unique neuron type.
# Print the unique neuron types.

neural_data = "excitatory, inhibitory, sensory, motor, inhibitory, sensory, excitatory"
neural_list = neural_data.split(',')
unique_neurons = list()

for neuron in neural_list:
    if neuron.strip() in unique_neurons:
        continue
    unique_neurons.append(neuron.strip())
print(unique_neurons)
