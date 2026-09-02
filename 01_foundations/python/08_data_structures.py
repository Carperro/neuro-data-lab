# Exercise 1 - Sets
# Create a program that:
# Convert neural_data into a list.
# Create a set from the list.
# Print the resulting set.
# Observe what happens to the repeated neuron types.

# neural_data = "excitatory, inhibitory, sensory, motor, inhibitory, sensory, excitatory"
# neural_list = neural_data.replace(',',' ').split() # → No es lo más óptimo, es mejor el pipeline para el tratamiento de datos
# seteado = set(neural_list) # → Vemos que el set no permite mutaciones ni duplicados
# print(seteado)

# Exercise 2 — Clean Unique Neuron Types
# Create a program that:
# Convert neural_data into a list using split(',').
# Create an empty list called clean_neurons.
# Loop through the list using for.
# Clean each neuron using strip() and lower().
# Add each cleaned neuron to clean_neurons using append().
# Convert clean_neurons into a set.
# Print the resulting set.

#neural_data = " EXCITATORY, inhibitory, SENSORY, motor, inhibitory, sensory, EXCITATORY "
#neural_list = neural_data.split(',')
#clean_neurons = list()
#for neuron in neural_list:
#    clean_neurons.append((neuron).lower().strip())
#unique_neurons = set(clean_neurons)
#print(unique_neurons)

# Exercise 2.5 - Dictionary Basics
# Create a dictionary called neuron_counts.
# Add these neuron types as keys:
# excitatory
# inhibitory
# sensory
# Give each key an initial value of 0.
# Then:
# 1. Print the dictionary.
# 2. Access the value of "inhibitory" and print it.
# 3. Increase the value of "inhibitory" by 1.
# 4. Print the dictionary again.

neuron_counts = {
    'excitatory': 0,
    'inhibitory': 0,
    'sensory':0
}
neuron_counts['inhibitory'] += 1
print(neuron_counts['inhibitory'])

# Exercise 3 — Unique Neuron Types Counter
# Goal: Create a dictionary that counts how many times each neuron type appears.

#neural_data = " EXCITATORY, inhibitory, sensory, motor, inhibitory, sensory, excitatory, motor, inhibitory "
#neural_list = neural_data.split(',')

    

