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

#neuron_counts = {
#    'excitatory': 0,
#    'inhibitory': 0,
#    'sensory':0
#}
#neuron_counts['inhibitory'] += 1
#print(neuron_counts['inhibitory'])

# Exercise 2.6 - Dictionary Manipulation:

# Create a dictionary called neuron_info.
# Add these keys:
# neuron_type
# firing_rate
# signal_strength
#
# Give them appropriate values.
#
# Then:
# 1. Print the dictionary.
# 2. Access the value of "firing_rate".
# 3. Change the firing_rate.
# 4. Add a new key called "status".
# 5. Print the dictionary again.

#neuron_info = {'neuron_type':0,'firing_rate':0,'signal_strength':0}
#print(neuron_info)
#neuron_info['firing_rate'] += 1     # → Añadimos un valor, en este caso no asignando sino incrementando
#neuron_info['firing_rate'] += 10    # → Incrementamos el valor de la key en + 10
#neuron_info['status'] = 0           # → Creamos una nueva key 
#print(neuron_info)

# Exercise 3 — Unique Neuron Types Counter
# Goal: Create a dictionary that counts how many times each neuron type appears.

#neural_data = " EXCITATORY, inhibitory, sensory, motor, inhibitory, sensory, excitatory, motor, inhibitory "
#neural_list = neural_data.split(',')
#neuron_counts = {}
#for neuron in neural_list:                      # → recorremos cada elemento
#    cleaned_neuron = neuron.lower().strip()     # → normalizamos el dato
#    if cleaned_neuron in neuron_counts:         # → pregunto si ya existe como key
#        neuron_counts[cleaned_neuron] += 1      # → si existe, aumento el value.    
#    else:
#        neuron_counts[cleaned_neuron] = 1       # → si no existe, creo la key con su primer conteo.
#print(neuron_counts)

# Exercise 3.1 — Neuron Population Counter
# Count how many times each neuron type appears.
# Use a dictionary called neuron_counts.
# Expected result:
# {'excitatory': 3, 'sensory': 2, 'inhibitory': 2, 'motor': 1}
# The data:
#neural_data = "excitatory, sensory, inhibitory, excitatory, motor, sensory, inhibitory, excitatory"
#neural_list = neural_data.split(',')
#neuron_count = {}
#for neuron in neural_list:
#    cleaned_neuron = neuron.strip()
#    if cleaned_neuron in neuron_count:
#        neuron_count[cleaned_neuron] += 1
#    else:
#        neuron_count[cleaned_neuron] = 1
#print(neuron_count)
    
# Exercise 4 — Neuron Tuple

# Create a tuple called neuron_data.
# Store these three values:
# neuron_type
# firing_rate
# signal_strength
# Then:
# 1. Print the tuple.
# 2. Access the second value.
# 3. Print its type.

neuron_data = ("neuron_type","firing_rate","signal_strength")
print(neuron_data)
print(neuron_data[0])
print(type(neuron_data))