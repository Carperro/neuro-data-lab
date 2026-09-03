# Exercise 1 — First Function
# Create a function called show_neuron_info().
# Inside the function:
# 1. Print "Neuron detected."
# 2. Print "Analyzing neural signal..."
# Then:
# 3. Call the function.

def show_neuron_info():
    print(f'[!] Neuron detected.')
    print(f'[*] Analyzing neural signal...')
#show_neuron_info()

# Exercise 2 — Neuron Signal
# Create a function called analyze_neuron().
# It should receive two parameters: neuron_type and firing_rate
# Inside the function:
# 1. Print the neuron type.
# 2. Print the firing rate.
# Then call the function with:
# neuron_type = "excitatory"
# firing_rate = 75

def analyze_neuron(neuron_type, firing_rate):
        print(f'[!] Neuron detected             → {neuron_type}')
        print(f'[*] Analyzing neural signal...  → {firing_rate}')
#analyze_neuron("excitatory",75)

# Exercise 3 — Analyze Signal
# Create a function called analyze_signal().
# It should receive: neuron_type ; signal_strength ;
# Inside the function:
# 1. If the neuron is "excitatory":
# - If signal_strength >= 70, print "Strong signal."
# - Otherwise, print "Weak signal."
# 2. If the neuron is "inhibitory":
# - If signal_strength >= 50, print "Strong signal."
# - Otherwise, print "Weak signal."
# Then test the function with:
# neuron_type = "excitatory"
# signal_strength = 75

def analyze_signal(neuron_type,signal_strength):
    if neuron_type == "excitatory":
        if signal_strength >= 70:
            print('[+] Strong signal...')
        else:
            print('[-] Weak signal...')
    if neuron_type == "inhibitory":
        if signal_strength >= 50:
            print('[+] Strong signal...')
        else:
            print('[-] Weak signal...')
#analyze_signal("excitatory",100)

#Exercise 4 — Return a Signal Classification
#Modify analyze_signal().
#Instead of printing "Strong signal." or "Weak signal.",
#return the corresponding string.
#Then:
        #1. Call the function.
        #2. Store the returned value in a variable called result.
        #3. Print result.

def analyze_signal(neuron_type,signal_strength):
    if neuron_type == "excitatory":
        if signal_strength >= 70:    
            return "strong" 
        else:
            return "weak" 
    elif neuron_type == "inhibitory":
        if signal_strength >= 50:    
            return "strong" 
        else:
            return "weak" 
results = analyze_signal("excitatory",10)

# Exercise 5 — Multiple Returns
# Create a function called classify_signal().
# It should receive: neuron_type ; signal_strength
# If neuron_type is "excitatory":
# - signal_strength >= 70 → return "Strong"
# - otherwise → return "Weak"
# If neuron_type is "inhibitory":
# - signal_strength >= 50 → return "Strong"
# - otherwise → return "Weak"
# Then test it with: 1. ("excitatory", 80) ; 2. ("excitatory", 40) ; 3. ("inhibitory", 60)

def classify_signal(neuron_type, signal_strength):
    if neuron_type == "excitatory":
        if signal_strength >= 70:
            return "strong"
        else:
            return "weak"
    elif neuron_type == "inhibitory":
        if signal_strength >= 50:
            return "strong"
        else:
            return "weak"

#results = classify_signal("excitatory", 80)
#print(f'[!] This neuron has a {results} signal...')
#results = classify_signal("excitatory", 40)
#print(f'[!] This neuron has a {results} signal...')
#results = classify_signal("inhibitory", 60)
#print(f'[!] This neuron has a {results} signal...')

# Exercise 6 — Return Neuron Data
# Create a function called get_neuron_info().
# It should receive: neuron_type ; firing_rate ; signal_strength
# The function should return all three pieces of information together.
# Then:
# 1. Call the function with:
#    "excitatory", 75, 90
# 2. Store the returned value in a variable called neuron_info.
# 3. Print neuron_info.
# 4. Print the type of neuron_info.

def get_neuron_info(neuron_type, firing_rate, signal_strength):
    neuron_info = {
        'neuron_type': neuron_type,
        'firing_rate': firing_rate,
        'signal_strength': signal_strength
    }
    return neuron_info
# results = get_neuron_info("excitatory",75,90)
# print(results)
# print(results['neuron_type'])

# Exercise 7 — Neural Population Analyzer
# Create a function called analyze_population().
# It should receive neural_data.
# The data contains different neuron types separated by commas.
# Some values may contain uppercase letters or extra spaces.
# The function should:
# - Clean and normalize the neuron types.
# - Count how many times each neuron type appears.
# - Determine the total number of neurons.
# - Determine how many different neuron types are present.
# - Return all the results together.
# Then:
# - Call the function.
# - Store the returned value.
# - Print the complete result.
# - Print the number of inhibitory neurons.
# - Print the total number of neurons.
# - Print the number of unique neuron types.
# Use this data:
#neural_data = " EXCITATORY, inhibitory, sensory, motor, inhibitory, sensory, excitatory, motor, inhibitory"
#def analyze_population(neural_data):
#    neuron_list = neural_data.split(',')
#    population_total = len(neuron_list)
#    unique_neurons = dict()
#    for neuron in neuron_list:
#        neuron_cleaned = neuron.lower().strip()
#        if neuron_cleaned in unique_neurons:
#            unique_neurons[neuron_cleaned] += 1
#        else:
#            unique_neurons[neuron_cleaned] = 1
#    neuron_types = len(unique_neurons)
#    results = {
#        'neuron_counts': unique_neurons,
#        'population_total': population_total,
#        'neuron_types': neuron_types
#    }
#    return results

#analyze_population_results = analyze_population(neural_data)
# print(analyze_population_results) # → Imprimimos todo el resultado, que es un diccionario
# print(analyze_population_results['neuron_types']) # → Accedemos a esa parte del diccionario que queremos saber específicamente
# print(analyze_population_results['population_total']) # → Accedemos a esa parte del diccionario que queremos saber específicamente
# print(analyze_population_results['neuron_counts']['inhibitory']) # → Accedemos a esa parte del diccionario que contiene otro diccionario
# Output printed ↓
#print(f"""
#            =======================================
#                  NEURAL POPULATION ANALYZER
#            =======================================
#    [+] Population total            : {analyze_population_results['population_total']}
#    [+] Neuron types                : {analyze_population_results['neuron_types']}
#    [+] Neuron counts:
#                - Excitatory        : {analyze_population_results['neuron_counts']['excitatory']}
#                - Inhibitory        : {analyze_population_results['neuron_counts']['inhibitory']}
#                - Sensory           : {analyze_population_results['neuron_counts']['sensory']}
#                - Motor             : {analyze_population_results['neuron_counts']['motor']}
#            =======================================
#      """)
        
# Exercise 8 - Neural Population Reporter
neural_data = " EXCITATORY, inhibitory, sensory, motor, inhibitory, sensory, excitatory, motor, inhibitory"

def analyze_population(neural_data):
    neuron_list = neural_data.split(',')
    population_total = len(neuron_list)
    unique_neurons = dict()
    for neuron in neuron_list:
        neuron_cleaned = neuron.lower().strip()
        if neuron_cleaned in unique_neurons:
            unique_neurons[neuron_cleaned] += 1
        else:
            unique_neurons[neuron_cleaned] = 1
    neuron_types = len(unique_neurons)
    results = {
        'neuron_counts': unique_neurons,
        'population_total': population_total,
        'neuron_types': neuron_types
    }
    return results

results = analyze_population(neural_data)

def report_population(analyze_population_results):
    for neuron,counter in analyze_population_results['neuron_counts'].items():
        print(f"Neuron type: {neuron} → {counter}")

report_population(results)

from collections import Counter


def analyze_population(neural_data: str) -> dict:
    """Analyze neuron types from comma-separated neural data."""
    neurons = [
        neuron.strip().lower()
        for neuron in neural_data.split(",")
        if neuron.strip()
    ]
    neuron_counts = Counter(neurons)
    return {
        "neuron_counts": dict(neuron_counts),
        "population_total": len(neurons),
        "neuron_types": len(neuron_counts),
    }

def report_population(results: dict) -> None:
    """Display a formatted neural population report."""
    print("\n=== Neural Population Report ===")
    print(f"Population total: {results['population_total']}")
    print(f"Neuron types: {results['neuron_types']}")
    print("\nNeuron counts:")
    for neuron_type, count in results["neuron_counts"].items():
        print(f"  - {neuron_type.capitalize()}: {count}")

neural_data = (
    " EXCITATORY, inhibitory, sensory, motor, "
    "inhibitory, sensory, excitatory, motor, inhibitory"
)
results = analyze_population(neural_data)

report_population(results)