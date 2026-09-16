# ===================================================
# MINI-PROYECTO — NEURAL SIGNAL ANALYZER
# ===================================================

# Cada registro contiene:
# (neuron_type, signal_strength)

neural_data = [
    ("excitatory", 72),
    ("inhibitory", 45),
    ("sensory", 88),
    ("excitatory", 61),
    ("inhibitory", 34),
    ("sensory", 95),
    ("unknown", 76),
    ("excitatory", -8),
    ("inhibitory", 67),
    ("sensory", 52),
    ("excitatory", 83),
    ("inhibitory", 71),
    ("sensory", 39),
    ("excitatory", 100),
    ("inhibitory", 58),
    ("sensory", -12),
    ("excitatory", 47),
    ("inhibitory", 89),
    ("sensory", 64),
    ("excitatory", 76),
    ("inhibitory", 42),
    ("sensory", 81),
    ("excitatory", 55),
    ("inhibitory", 73),
    ("sensory", 68),
    ("excitatory", 91),
    ("inhibitory", 63),
    ("sensory", 49),
    ("excitatory", 37),
    ("inhibitory", 86),
    ("sensory", 77),
    ("excitatory", 69),
    ("inhibitory", 51),
    ("sensory", 93),
    ("excitatory", 105),
    ("inhibitory", 80),
    ("sensory", 74),
    ("excitatory", 62)
]
# ===================================================
# VALIDATION RULES
# ===================================================
# Tipos de neurona aceptados.
neuron_types_allowed = {"excitatory","inhibitory","sensory"}
# ===================================================
# VALIDATE DATA
# ===================================================
def validation(neural_data):
    valid_neurons = []                                  # Guardamos los registros válidos.
    invalid_population = []                             # Guardamos los registros inválidos.
    for neuron in neural_data:                          # Revisamos cada registro del dataset.
        neuron_type = neuron[0]                         # Extraemos sus dos valores.
        signal_strength = neuron[1]
        if (neuron_type in neuron_types_allowed and 0 < signal_strength <= 100):            # Un registro es válido si cumple ambas reglas.
            valid_neurons.append(neuron)                # Guardamos el registro válido.
        else:
            invalid_population.append(neuron)           # Conservamos los registros inválidos.
    return valid_neurons, invalid_population            # Devolvemos ambas poblaciones.
neural_population = validation(neural_data)             # Ejecutamos la validación.
# ===================================================
# CLASSIFY SIGNAL STRENGTH
# ===================================================
def classify_strength(signal_strength):
    if signal_strength > 70:                            # Clasificamos la señal según nuestro umbral.
        return "strong"
    return "weak"
# ===================================================
# GET INVALID REASONS
# ===================================================
def get_invalid_reasons(neuron_type, signal_strength):
    reasons = []
    if neuron_type not in neuron_types_allowed:         # Comprobamos si el tipo no está permitido.
        reasons.append("invalid neuron type")
    if signal_strength <= 0:                            # Comprobamos si la señal es demasiado baja.
        reasons.append("signal too low")
    if signal_strength > 100:                           # Comprobamos si la señal es demasiado alta.
        reasons.append("signal too high")
    return reasons                                      # Devolvemos todas las razones encontradas.
# ===================================================
# ENRICH INDIVIDUAL DATA
# ===================================================
def enrich_neuron(neuron, invalid=False):
    neuron_type = neuron[0]                             # Extraemos los datos originales.
    signal_strength = neuron[1]
    neuron_info = {                                     # Creamos la información enriquecida.
        "neuron_type": neuron_type,
        "signal_strength": signal_strength,
        "strength": classify_strength(signal_strength)
    }
    if invalid:                                         # Los registros inválidos necesitan además conocer las razones de invalidación.
        neuron_info["reasons"] = get_invalid_reasons(neuron_type,signal_strength)
    return neuron_info                                  # Devolvemos la neurona enriquecida.
# ===================================================
# ANALYZE INDIVIDUAL NEURONS
# ===================================================
def analyze_population(neural_population):
    valid_population = neural_population[0]                 # Separamos las dos poblaciones.    
    invalid_population = neural_population[1]               
    info_valid_neurons = []                                 # Guardamos la información enriquecida de las válidas.
    info_invalid_neurons = []                               # Guardamos la información enriquecida de las inválidas.
    for neuron in valid_population:                         # Procesamos cada neurona válida.
        neuron_info = enrich_neuron(neuron)                 # Enriquecemos el registro.
        info_valid_neurons.append(neuron_info)              # Guardamos el resultado.
    for neuron in invalid_population:                       # Procesamos cada neurona inválida.
        neuron_info = enrich_neuron(neuron,invalid=True)    # Enriquecemos el registro y calculamos sus razones.
        info_invalid_neurons.append(neuron_info)            # Guardamos el resultado.
    analysis = {                                            # Construimos la salida estructurada.    
        "valid_population": info_valid_neurons,
        "invalid_population": info_invalid_neurons,
        "valid_count": len(info_valid_neurons),
        "invalid_count": len(info_invalid_neurons)
    }
    return analysis                                         # Devolvemos la información enriquecida.
analyze_population_report = analyze_population(neural_population)        # Ejecutamos el análisis individual.
# ===================================================
# SIGNAL STATISTICS
# ===================================================
def signal_statistics(signals):
    if not signals:                                         # Si no existen señales, evitamos errores matemáticos.
        return {
            "sum": 0,
            "average": None,
            "highest": None,
            "lowest": None
        }
    signal_sum = sum(signals)                               # Calculamos la suma.
    signal_average = round(signal_sum / len(signals),2)     # Calculamos el promedio.
    highest_signal = max(signals)                           # Buscamos la señal más alta.
    lowest_signal = min(signals)                            # Buscamos la señal más baja.
    return {"sum": signal_sum,"average": signal_average,"highest": highest_signal,"lowest": lowest_signal}      # Devolvemos todas las estadísticas.
# ===================================================
# SPLIT SIGNALS BY STRENGTH
# ===================================================
def split_by_strength(population):
    signals = []                                            # Lista con todos los signals.
    strong_signals = []                                     # Signals strong.        
    weak_signals = []                                       # Signals weak.
    for neuron in population:                               # Recorremos cada neurona.    
        signal_strength = neuron["signal_strength"]         # Extraemos signal.
        signals.append(signal_strength)                     # Guardamos el signal general.    
        if neuron["strength"] == "strong":                  # Separamos según la clasificación ya calculada.
            strong_signals.append(signal_strength)
        else:
            weak_signals.append(signal_strength)                
    return signals, strong_signals, weak_signals            # Devolvemos las tres colecciones.
# ===================================================
# GROUP BY NEURON TYPE
# ===================================================
def group_by_type(population):
    groups = {}                                             # Empezamos con un diccionario vacío.
    for neuron in population:                               # Recorremos la población.
        neuron_type = neuron["neuron_type"]                 # Extraemos el tipo.    
        if neuron_type not in groups:                       # Si el tipo todavía no existe, creamos su lista.
            groups[neuron_type] = []
        groups[neuron_type].append(neuron)                  # Guardamos la neurona en su grupo.
    return groups                                           # Devolvemos los grupos.
# ===================================================
# COUNT INVALID REASONS
# ===================================================
def count_reasons(population):
    reasons_count = {}                                   # Diccionario para acumular cada problema.
    for neuron in population:                            # Recorremos los registros inválidos.
        for reason in neuron.get("reasons", []):         # Cada neurona puede tener más de una razón.
            if reason not in reasons_count:              # Si es la primera aparición, empezamos en cero.
                reasons_count[reason] = 0
            reasons_count[reason] += 1                   # Sumamos una aparición.
    return reasons_count                                 # Devolvemos el conteo.
# ===================================================
# POPULATION ANALYSIS
# ===================================================
def population_analyzer(analyze_population_report):
    valid_population_data = (analyze_population_report["valid_population"])         # Recuperamos las poblaciones enriquecidas.
    invalid_population_data = (analyze_population_report["invalid_population"])
    # ---------------------------------------------------
    # GLOBAL DATA
    # ---------------------------------------------------
    total_records = (len(valid_population_data)+ len(invalid_population_data))      # Cantidad total de registros.
    valid_count = len(valid_population_data)                                        # Cantidad válida.
    invalid_count = len(invalid_population_data)                                    # Cantidad inválida.
    if total_records:                                                               # Calculamos los porcentajes globales.        
        valid_percentage = round((valid_count / total_records) * 100,2)
        invalid_percentage = round((invalid_count / total_records) * 100,2)
    else:
        valid_percentage = 0
        invalid_percentage = 0
    # ---------------------------------------------------
    # VALID POPULATION
    # ---------------------------------------------------
    (valid_signals,valid_strong_signals,valid_weak_signals) = split_by_strength(valid_population_data)     # Extraemos signals y los separamos por strength.
    valid_by_type = group_by_type(valid_population_data)                             # Agrupamos las válidas por neuron type.           
    valid_stats = signal_statistics(valid_signals)                                   # Calculamos estadísticas de signals válidos.
    # ---------------------------------------------------
    # INVALID POPULATION
    # ---------------------------------------------------
    (invalid_signals,invalid_strong_signals,invalid_weak_signals) = split_by_strength(invalid_population_data) # Extraemos signals inválidos y los clasificamos.
    invalid_by_type = group_by_type(invalid_population_data)                         # Agrupamos las inválidas por neuron type.
    invalid_reasons = count_reasons(invalid_population_data)                         # Contamos las razones de invalidación.
    invalid_stats = signal_statistics(invalid_signals)                               # Calculamos estadísticas de signals inválidos.
    # ---------------------------------------------------
    # FINAL RESULT
    # ---------------------------------------------------
    analysis = {                                                # Construimos el resultado final.
        "global": {                                             # Información global.
            "total_records": total_records,
            "valid_count": valid_count,
            "invalid_count": invalid_count,
            "valid_percentage": valid_percentage,
            "invalid_percentage": invalid_percentage
        },
        "valid": {                                              # Información de válidas.    
            "neurons": valid_population_data,
            "signals": valid_signals,
            "strong_signals": valid_strong_signals,
            "weak_signals": valid_weak_signals,
            "strong_count": len(valid_strong_signals),
            "weak_count": len(valid_weak_signals),
            "by_type": valid_by_type,
            "signal_sum": valid_stats["sum"],
            "signal_average": valid_stats["average"],
            "highest_signal": valid_stats["highest"],
            "lowest_signal": valid_stats["lowest"]
        },
        "invalid": {                                            # Información de inválidas.
            "neurons": invalid_population_data,
            "signals": invalid_signals,
            "strong_signals": invalid_strong_signals,
            "weak_signals": invalid_weak_signals,
            "strong_count": len(invalid_strong_signals),
            "weak_count": len(invalid_weak_signals),
            "by_type": invalid_by_type,
            "reasons": invalid_reasons,
            "signal_sum": invalid_stats["sum"],
            "signal_average": invalid_stats["average"],
            "highest_signal": invalid_stats["highest"],
            "lowest_signal": invalid_stats["lowest"]
        }
    }
    return analysis                                             # Devolvemos todo el análisis.

result = population_analyzer(analyze_population_report)         # Analizamos ambas poblaciones.    

def average_calculator(population):                             # Extraemos el promedio de las señales de cada población
    signals = []
    for signal in population:
        signals.append(signal["signal_strength"])
    if not signals:
        return
    average = sum(signals) / len(signals)
    return average

print(result)

# Luego volveremos para ir refactorizando el código y hacer un programa funcional










