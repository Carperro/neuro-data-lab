# Functions 2.0

# Exercise 1 - Neural Signal Filter

# Create a function called filter_neurons()
# The function should receive a list of neuron dictionaries
# Each neuron contains:
    # neuron_type
    # firing_rate
    # signal_strength
# The function should:
# Return only the neurons whose signal_strength is 70 or higher
# Use the provided neurons data
# Call the function
# Store the returned result
# Print the result
# Print how many neurons passed the filter
# Data: 
neurons = [
    {
        "neuron_type": "excitatory",
        "firing_rate": 80,
        "signal_strength": 60
    },
    {
        "neuron_type": "inhibitory",
        "firing_rate": 60,
        "signal_strength": 43
    },
    {
        "neuron_type": "excitatory",
        "firing_rate": 80,
        "signal_strength": 50
    },
    {
        "neuron_type": "inhibitory",
        "firing_rate": 60,
        "signal_strength": 80
    },
    {
        "neuron_type": "excitatory",
        "firing_rate": 80,
        "signal_strength": 67
    },
    {
        "neuron_type": "inhibitory",
        "firing_rate": 60,
        "signal_strength": 44
    },
    {
        "neuron_type": "sensory",
        "firing_rate": 50,
        "signal_strength": 72
    },
    {
        "neuron_type": "motor",
        "firing_rate": 70,
        "signal_strength": 56
    },
    {
        "neuron_type": "motor",
        "firing_rate": 70,
        "signal_strength": 65
    },
    {
        "neuron_type": "motor",
        "firing_rate": 70,
        "signal_strength": 50
    },
    {
        "neuron_type": "interneuron",
        "firing_rate": 80,
        "signal_strength": 95
    },
    {
        "neuron_type": "interneuron",
        "firing_rate": 80,
        "signal_strength": 45
    },
    {
        "neuron_type": "interneuron",
        "firing_rate": 80,
        "signal_strength": 55
    },
    {
        "neuron_type": "interneuron",
        "firing_rate": 80,
        "signal_strength": 75
    },
    {
        "neuron_type": "motor",
        "firing_rate": 70,
        "signal_strength": 55
    }
]
def filter_neurons(neurons):                # Defino la funcion y argumento
    valid_neurons = list()                  # Creo una lista vacía para ir almacenando las neuronas validas
    for neuron in neurons:                  # Creo un bucle for in para iterar cada elemento
        if neuron['signal_strength'] >= 70: # Accedo al diccionario y a su valor a través de la key y hago la comparación
            valid_neurons.append(neuron)    # Si se cumple la condición la añado a la lista vacía con append()
    return valid_neurons                    # Retorno la lista con las neuronas válidas
filter_results = filter_neurons(neurons)    # Calleo la función
#print(filter_results)                      # Imprimo los resultados
#print(f'[!] Cantidad de neuronas que pasaron el resultado: {len(filter_results)}') # Imprimo la cantidad de neuronas que pasaron el filtro
        
# Exercise 2 - Neuron Type Analyzer
# Create a function called analyze_neuron_types()
# The function should receive a list of neuron dictionaries
# Each neuron contains: neuron_type ; firing_rate ; signal_strength
# The function should:
    # Determine how many neurons belong to each neuron type
    # Return the results
    # Use the provided neurons data
    # Call the function
    # Store the returned result and then print the result

def analyze_neuron_types(neurons):                      # Definimos la función
    types_and_counter = {}                              # Creamos un diccionario vacío para almacenar el tipo de neurona y la cantidad
    for neuron in neurons:                              # Creamos un bucle para iterar entre cada neurona y ver sus propiedades
        neuron_types = neuron['neuron_type']            # Almacenamos el tipo de neurona "excitatory" en una variable
        if neuron_types in types_and_counter:           # Consultamos si "excitatory" está en el nuevo diccionario, si está sumamos uno.
            types_and_counter[neuron_types] += 1        # Aumentamos el value del tipo de neurona
        else:                                           # Si no está, creamos la entrada y le asignamos valor 1
            types_and_counter[neuron_types] = 1         # Aumentamos el value del tipo de neurona
    return types_and_counter                            # Retornamos el resultado
results = analyze_neuron_types(neurons)                 # Llamamos a la función
print(results)                                          # Imprimimos los resultados
        
# Exercise 3 - Neuron Signal Statistics

# Create a function called calculate_signal_statistics()
# The function should receive the same list of neuron dictionaries.
# Each neuron contains: neuron_type; firing_rate; signal_strength
# The function should:
# - Calculate the average signal_strength.
# - Find the strongest signal.
# - Find the weakest signal.
# - Return all three results together.
# Then:
# - Call the function.
# - Store the returned result.
# - Print the result.

def calculate_signal_statistics(neurons):
    signals_counter = 0
    signals = list()
    for neuron in neurons:
        signals.append(neuron['signal_strength'])  
    for average in signals:
        signals_counter += average
    average_signal = signals_counter / len(signals)        
    signals.sort()
    weakest_signal = signals[0]
    strongest_signal = signals[-1]
    results = [average_signal, weakest_signal, strongest_signal]
    return results 

results = calculate_signal_statistics(neurons)

print(f"[!] The average signal is: {results[0]}\n[!] The weakest signal is: {results[1]}\n[!] The strongest signal is: {results[2]}")
