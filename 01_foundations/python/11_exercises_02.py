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
# results = analyze_neuron_types(neurons)                 # Llamamos a la función
# print(results)                                          # Imprimimos los resultados
        
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

#results = calculate_signal_statistics(neurons)
#print(f"[!] The average signal is: {results[0]}\n[!] The weakest signal is: {results[1]}\n[!] The strongest signal is: {results[2]}")

# Exercise 4 - Integration Challenge — Neural Population Statistics
# Create a function analyze_signals(neurons)
# It should determine:
    # - total number of neurons
    # - average signal strength
    # - weakest signal
    # - strongest signal
# Return all four results together.
neurons = [
    {"type": "excitatory", "signal_strength": 72},
    {"type": "inhibitory", "signal_strength": 35},
    {"type": "sensory", "signal_strength": 91},
    {"type": "excitatory", "signal_strength": 64},
    {"type": "inhibitory", "signal_strength": 58},
    {"type": "sensory", "signal_strength": 47},
]

def analyze_signals(neurons):
    str_sum = 0
    for index,neuron in enumerate(neurons):
        str_sum += neuron["signal_strength"]
        if index == 0:
            strongest = neuron["signal_strength"]  
            weakest = neuron["signal_strength"] 
        else:
            if neuron["signal_strength"] > strongest:
                strongest = neuron["signal_strength"]
            if neuron["signal_strength"] < weakest:
                weakest = neuron["signal_strength"]
    results = {
        "number_of_neurons": len(neurons),
        "average_signal": round(str_sum / len(neurons),2),
        "highest_signal": strongest,
        "weakest_signal": weakest
    }
    return results
    
#analyzer_signals = analyze_signals(neurons)
#print(analyzer_signals)
    
# Exercise 5 — Neuron Classification Pipeline
# Create a function: classify_neuron(neuron)
# It should return: 
    # "strong" if signal_strength >= 70
    # "weak" if signal_strength < 70
    # "invalid" if the neuron_type is not excitatory, inhibitory or sensory
# Then create: analyze_population(neurons)
# This function should:
    # Procces every neuron:
    # Use classify_neuron() to classify it:
    # Count:
            # Total valid neurons
            # Strong neurons
            # Weaks neurons
            # Invalid neurons
    # Return all results in a dictionary.

# Dataset: 
neurons = [
    {"type": "excitatory", "signal_strength": 72},
    {"type": "inhibitory", "signal_strength": 35},
    {"type": "sensory", "signal_strength": 91},
    {"type": "excitatory", "signal_strength": 64},
    {"type": "inhibitory", "signal_strength": 58},
    {"type": "sensory", "signal_strength": 47},
    {"type": "unknown", "signal_strength": 80},
    {"type": "excitatory", "signal_strength": 105},
]

def classify_neuron(neuron):
    valid_neurons = ["excitatory","inhibitory","sensory"]
    if neuron["type"] in valid_neurons:
        if neuron["signal_strength"] >= 70:
            return "strong"
        else:
            return "weak"
    else: return "invalid"

def analyze_population(neurons):
    strong_neurons = 0
    invalid_neurons = 0
    weak_neurons = 0
    for neuron in neurons:
        classifier = classify_neuron(neuron)
        if classifier == "strong":
            strong_neurons += 1
        elif classifier == "invalid":
            invalid_neurons += 1
        else: 
            weak_neurons += 1
    result = {
        "strong_neurons": strong_neurons,
        "invalid_neurons": invalid_neurons,
        "weak_neurons": weak_neurons,
        "total_valid_neurons": (strong_neurons + weak_neurons)
    }
    return result

#exercise_result = analyze_population(neurons)
#print(exercise_result)

# Exercise 6 - Neural Population Report
# The function should return a dictionary containing:
    # total number of neurons
    # average signal strength
    # strongest signal
    # weakest signal
    # number of neurons by type
    # number of strong neurons
    # number of weak neurons
# Requirements
    # Reuse classify_neuron().
    # Use at least one helper function you've already created.
    # Process the population with a loop.
    # Return one structured dictionary.
    # Do not use min(), max(), or sum() for the main analysis. Use the reasoning patterns we've been practicing.
    
neurons = [
    {"type": "excitatory", "signal_strength": 72},
    {"type": "inhibitory", "signal_strength": 35},
    {"type": "sensory", "signal_strength": 91},
    {"type": "excitatory", "signal_strength": 64},
    {"type": "inhibitory", "signal_strength": 58},
    {"type": "sensory", "signal_strength": 47},
    {"type": "excitatory", "signal_strength": 83},
    {"type": "inhibitory", "signal_strength": 76},
    {"type": "sensory", "signal_strength": 29},
]

def neural_population_report(neurons):
    signals = []
    total_signals = 0
    counter_by_type = {
        "excitatory": 0,
        "inhibitory": 0,
        "sensory": 0,
    }
    counter_by_classify = {
        "weaks": 0,
        "strongs": 0,
    }
    for neuron in neurons:
        neuron_classified = classify_neuron(neuron)
        if neuron_classified == "invalid":
            continue
        total_signals += neuron["signal_strength"]
        signals.append(neuron["signal_strength"])
        if neuron_classified == "invalid":
            continue
        if neuron_classified == "weak":
            counter_by_classify["weaks"] += 1
        else:
            counter_by_classify["strongs"] += 1

        if neuron["type"] == "sensory":
            counter_by_type["sensory"] += 1
        elif neuron["type"] == "excitatory":
            counter_by_type["excitatory"] += 1
        else:
            counter_by_type["inhibitory"] += 1
    signal_sorted = sorted(signals)
    
    to_output = {
        "total_neurons": len(neurons),
        "average_signal": total_signals/len(neurons),
        "strongest_signal": signal_sorted[-1],
        "weakest_signal": signal_sorted[0],
        "n_neurons_by_type":counter_by_type,
        "n_strong_neurons": counter_by_classify["strongs"],
        "n_weak_neurons": counter_by_classify["weaks"],
    }
    return to_output

resultados = neural_population_report(neurons)
print(resultados)