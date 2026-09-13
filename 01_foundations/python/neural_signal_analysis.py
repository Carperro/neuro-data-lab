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
    # Guardamos los registros válidos.
    valid_neurons = []
    # Guardamos los registros inválidos.
    invalid_population = []
    # Revisamos cada registro del dataset.
    for neuron in neural_data:
        # Extraemos sus dos valores.
        neuron_type = neuron[0]
        signal_strength = neuron[1]
        # Un registro es válido si cumple ambas reglas.
        if (neuron_type in neuron_types_allowed and 0 < signal_strength <= 100):
            # Guardamos el registro válido.
            valid_neurons.append(neuron)
        else:
            # Conservamos los registros inválidos.
            invalid_population.append(neuron)
    # Devolvemos ambas poblaciones.
    return valid_neurons, invalid_population
# Ejecutamos la validación.
neural_population = validation(neural_data)
# ===================================================
# CLASSIFY SIGNAL STRENGTH
# ===================================================
def classify_strength(signal_strength):
    # Clasificamos la señal según nuestro umbral.
    if signal_strength > 70:
        return "strong"
    return "weak"
# ===================================================
# GET INVALID REASONS
# ===================================================
def get_invalid_reasons(neuron_type, signal_strength):
    # Empezamos con una lista vacía de problemas.
    reasons = []
    # Comprobamos si el tipo no está permitido.
    if neuron_type not in neuron_types_allowed:
        reasons.append("invalid neuron type")
    # Comprobamos si la señal es demasiado baja.
    if signal_strength <= 0:
        reasons.append("signal too low")
    # Comprobamos si la señal es demasiado alta.
    if signal_strength > 100:
        reasons.append("signal too high")
    # Devolvemos todas las razones encontradas.
    return reasons
# ===================================================
# ENRICH INDIVIDUAL DATA
# ===================================================
def enrich_neuron(neuron, invalid=False):
    # Extraemos los datos originales.
    neuron_type = neuron[0]
    signal_strength = neuron[1]
    # Creamos la información enriquecida.
    neuron_info = {
        "neuron_type": neuron_type,
        "signal_strength": signal_strength,
        "strength": classify_strength(signal_strength)
    }
    # Los registros inválidos necesitan además
    # conocer las razones de invalidación.
    if invalid:
        neuron_info["reasons"] = get_invalid_reasons(neuron_type,signal_strength)
    # Devolvemos la neurona enriquecida.
    return neuron_info
# ===================================================
# ANALYZE INDIVIDUAL NEURONS
# ===================================================
def analyze_population(neural_population):
    # Separamos las dos poblaciones.
    valid_population = neural_population[0]
    invalid_population = neural_population[1]
    # Guardamos la información enriquecida de las válidas.
    info_valid_neurons = []
    # Guardamos la información enriquecida de las inválidas.
    info_invalid_neurons = []
    # Procesamos cada neurona válida.
    for neuron in valid_population:
        # Enriquecemos el registro.
        neuron_info = enrich_neuron(neuron)
        # Guardamos el resultado.
        info_valid_neurons.append(neuron_info)
    # Procesamos cada neurona inválida.
    for neuron in invalid_population:
        # Enriquecemos el registro y calculamos sus razones.
        neuron_info = enrich_neuron(neuron,invalid=True)
        # Guardamos el resultado.
        info_invalid_neurons.append(neuron_info)

    # Construimos la salida estructurada.
    analysis = {
        "valid_population": info_valid_neurons,
        "invalid_population": info_invalid_neurons,
        "valid_count": len(info_valid_neurons),
        "invalid_count": len(info_invalid_neurons)
    }

    # Devolvemos la información enriquecida.
    return analysis
# Ejecutamos el análisis individual.
analyze_population_report = analyze_population(neural_population)
# ===================================================
# SIGNAL STATISTICS
# ===================================================
def signal_statistics(signals):
    # Si no existen señales, evitamos errores matemáticos.
    if not signals:
        return {
            "sum": 0,
            "average": None,
            "highest": None,
            "lowest": None
        }
    # Calculamos la suma.
    signal_sum = sum(signals)
    # Calculamos el promedio.
    signal_average = round(signal_sum / len(signals),2)
    # Buscamos la señal más alta.
    highest_signal = max(signals)
    # Buscamos la señal más baja.
    lowest_signal = min(signals)
    # Devolvemos todas las estadísticas.
    return {"sum": signal_sum,"average": signal_average,"highest": highest_signal,"lowest": lowest_signal}
# ===================================================
# SPLIT SIGNALS BY STRENGTH
# ===================================================
def split_by_strength(population):
    # Lista con todos los signals.
    signals = []
    # Signals strong.
    strong_signals = []
    # Signals weak.
    weak_signals = []
    # Recorremos cada neurona.
    for neuron in population:
        # Extraemos signal.
        signal_strength = neuron["signal_strength"]
        # Guardamos el signal general.
        signals.append(signal_strength)
        # Separamos según la clasificación ya calculada.
        if neuron["strength"] == "strong":
            strong_signals.append(signal_strength)
        else:
            weak_signals.append(signal_strength)
    # Devolvemos las tres colecciones.
    return signals, strong_signals, weak_signals
# ===================================================
# GROUP BY NEURON TYPE
# ===================================================
def group_by_type(population):
    # Empezamos con un diccionario vacío.
    groups = {}
    # Recorremos la población.
    for neuron in population:
        # Extraemos el tipo.
        neuron_type = neuron["neuron_type"]
        # Si el tipo todavía no existe, creamos su lista.
        if neuron_type not in groups:
            groups[neuron_type] = []
        # Guardamos la neurona en su grupo.
        groups[neuron_type].append(neuron)
    # Devolvemos los grupos.
    return groups
# ===================================================
# COUNT INVALID REASONS
# ===================================================
def count_reasons(population):
    # Diccionario para acumular cada problema.
    reasons_count = {}
    # Recorremos los registros inválidos.
    for neuron in population:
        # Cada neurona puede tener más de una razón.
        for reason in neuron.get("reasons", []):
            # Si es la primera aparición, empezamos en cero.
            if reason not in reasons_count:
                reasons_count[reason] = 0
            # Sumamos una aparición.
            reasons_count[reason] += 1
    # Devolvemos el conteo.
    return reasons_count
# ===================================================
# POPULATION ANALYSIS
# ===================================================
def population_analyzer(analyze_population_report):
    # Recuperamos las poblaciones enriquecidas.
    valid_population_data = (analyze_population_report["valid_population"])
    invalid_population_data = (analyze_population_report["invalid_population"])
    # ---------------------------------------------------
    # GLOBAL DATA
    # ---------------------------------------------------
    # Cantidad total de registros.
    total_records = (len(valid_population_data)+ len(invalid_population_data))
    # Cantidad válida.
    valid_count = len(valid_population_data)
    # Cantidad inválida.
    invalid_count = len(invalid_population_data)
    # Calculamos los porcentajes globales.
    if total_records:
        valid_percentage = round((valid_count / total_records) * 100,2)
        invalid_percentage = round((invalid_count / total_records) * 100,2)
    else:
        valid_percentage = 0
        invalid_percentage = 0
    # ---------------------------------------------------
    # VALID POPULATION
    # ---------------------------------------------------

    # Extraemos signals y los separamos por strength.
    (valid_signals,valid_strong_signals,valid_weak_signals) = split_by_strength(valid_population_data)

    # Agrupamos las válidas por neuron type.
    valid_by_type = group_by_type(valid_population_data)
    # Calculamos estadísticas de signals válidos.
    valid_stats = signal_statistics(valid_signals)

    # ---------------------------------------------------
    # INVALID POPULATION
    # ---------------------------------------------------

    # Extraemos signals inválidos y los clasificamos.
    (invalid_signals,invalid_strong_signals,invalid_weak_signals) = split_by_strength(invalid_population_data)

    # Agrupamos las inválidas por neuron type.
    invalid_by_type = group_by_type(invalid_population_data)

    # Contamos las razones de invalidación.
    invalid_reasons = count_reasons(invalid_population_data)

    # Calculamos estadísticas de signals inválidos.
    invalid_stats = signal_statistics(invalid_signals)

    # ---------------------------------------------------
    # FINAL RESULT
    # ---------------------------------------------------
    # Construimos el resultado final.
    analysis = {
        # Información global.
        "global": {
            "total_records": total_records,
            "valid_count": valid_count,
            "invalid_count": invalid_count,
            "valid_percentage": valid_percentage,
            "invalid_percentage": invalid_percentage
        },
        # Información de válidas.
        "valid": {
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
        # Información de inválidas.
        "invalid": {
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
    # Devolvemos todo el análisis.
    return analysis
# ===================================================
# RUN FINAL ANALYSIS
# ===================================================
# Analizamos ambas poblaciones.
result = population_analyzer(analyze_population_report)
# ===================================================
# TEMPORARY TEST
# ===================================================
# Por ahora solamente comprobamos el resultado.
print(result)












