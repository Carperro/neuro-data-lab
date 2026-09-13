neural_data = [("excitatory", 72),("inhibitory", 45),("sensory", 88),("excitatory", 61),("inhibitory", 34),("sensory", 95),("unknown", 76),("excitatory", -8),("inhibitory", 67),("sensory", 52),("excitatory", 83),("inhibitory", 71),("sensory", 39),("excitatory", 100),("inhibitory", 58),("sensory", -12),("excitatory", 47),("inhibitory", 89),("sensory", 64),("excitatory", 76),("inhibitory", 42),("sensory", 81),("excitatory", 55),("inhibitory", 73),("sensory", 68),("excitatory", 91),("inhibitory", 63),("sensory", 49),("excitatory", 37),("inhibitory", 86),("sensory", 77),("excitatory", 69),("inhibitory", 51),("sensory", 93),("excitatory", 105),("inhibitory", 80),("sensory", 74),("excitatory", 62)]
neuron_types_allowed = {"excitatory","inhibitory","sensory"}

# VALIDATION

def validation(neural_data):
    invalid_population = []
    valid_neurons = []
    for neuron in neural_data:
        if neuron[0] in neuron_types_allowed:       # Filter by neuron_type
            if 0 < neuron[1] <= 100: 
                valid_neurons.append((neuron[0], neuron[1]))
            else:
                invalid_population.append((neuron[0], neuron[1]))
        else:
            invalid_population.append((neuron[0], neuron[1]))
    return valid_neurons,invalid_population

neural_population = validation(neural_data)

# POPULATION ANALYSIS
def analyze_population(neural_population):
    # Separate populations
    valid_population = neural_population[0]
    invalid_population = neural_population[1]
# -----------------------------------------------
    # VALID POPULATION
# -----------------------------------------------
    info_valid_neurons = []
    valids_counter = 0
    for neuron in valid_population:
        valids_counter += 1
        neuron_type = neuron[0]
        signal_strength = neuron[1]
        if signal_strength > 70:
            strength = "strong"
        else:
            strength = "weak"
        neuron_info = {
            "neuron_type": neuron_type,
            "signal_strength": signal_strength,
            "strength": strength
        }
        info_valid_neurons.append(neuron_info)    
# -----------------------------------------------
    # INVALID POPULATION
# -----------------------------------------------
    info_invalid_neurons = []
    invalids_counter = 0
    for neuron in invalid_population:
        invalids_counter += 1
        neuron_type = neuron[0]
        signal_strength = neuron[1]
        if signal_strength > 70:
            strength = "strong"
        else:
            strength = "weak"
        reasons = []
        if neuron_type not in neuron_types_allowed:
            reasons.append("invalid neuron type")
        if signal_strength <= 0:
            reasons.append("signal too low")
        if signal_strength > 100:
            reasons.append("signal too high")
   
        neuron_info = {
            "neuron_type": neuron_type,
            "signal_strength": signal_strength,
            "strength": strength,
            "reasons": reasons
        }
        info_invalid_neurons.append(neuron_info) 
# -----------------------------------------------
    # ANALYSIS OUTPUT
# -----------------------------------------------
    analysis = {
        "valid_population": info_valid_neurons,
        "invalid_population": info_invalid_neurons,
        "valid_count": valids_counter,
        "invalid_count": invalids_counter
    }
    return analysis
analyze_population_report = analyze_population(neural_population)
print(analyze_population(neural_population))














def population_analyzer(analyze_population_report):
    
    valid_population_data = analyze_population_report["valid_population"]      # Obtenemos los datos de la población válida
    invalid_population_data = analyze_population_report["invalid_population"]  # Obtenemos los datos de la población inválida
# -----------------------------------------------
    # GLOBAL DATA                               # Obtenemos algunos datos del la población total
# -----------------------------------------------
    total_records = (len(valid_population_data)+ len(invalid_population_data))  # Sumamos las neuronas válidas e inválidas para obtener la cantidad total de registros analizados
    valid_count = len(valid_population_data)            # Contamos directamente cuántos registros son válidos. 
    invalid_count = len(invalid_population_data)        # Y cuántos registros son inválidos. 
    if total_records > 0:                               # Obtenemos los porcentajes de ambos
        valid_percentage = round(
            (valid_count / total_records) * 100,2)
        invalid_percentage = round(
            (invalid_count / total_records) * 100,2)
    else:
        valid_percentage = 0                             # Guardamos los resultados
        invalid_percentage = 0                           # Guardamos los resultados
# -----------------------------------------------
    # VALID POPULATION
# -----------------------------------------------
    valid_signals = []
    valid_strong_signals = []
    valid_weak_signals = []
    valid_by_type = {
        "excitatory": [],
        "inhibitory": [],
        "sensory": []
    }
    for neuron in valid_population_data:
        neuron_type = neuron["neuron_type"]
        signal_strength = neuron["signal_strength"]
        strength = neuron["strength"]
        valid_signals.append(signal_strength)
        if strength == "strong":
            valid_strong_signals.append(signal_strength)
        else:
            valid_weak_signals.append(signal_strength)
        valid_by_type[neuron_type].append(neuron)    

result = population_analyzer(analyze_population_report)











    

