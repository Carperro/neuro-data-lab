# Exercise 1 - Number Classification
# Create a function called classify number
# The function should receive one number.
# Determinate wheter the number is: possitive, negateive, zero
# Then determinate wheter it is: even, odd
# Return all the results together.
# Test the function with al least 4 different numbers.
# Print the results. 

def classify_number(number): 
    even_and_odd = number % 2 
    if number == 0:
        return "Zero is even"
    elif number < 0:
        if even_and_odd == 0:
            return "Negative and even"
        else:
            return "Negative and odd"
    else:
        if even_and_odd == 0:
            return "Positive and even"
        else:
            return "Positive and odd"
#results = classify_number(-10)
#print(results)
    
## Exercise 2 — Basic Statistics
# Create a function called calculate_statistics().
# The function should receive a list of numbers.
# Determine:
#   - the total
#   - the average
#   - the highest value
#   - the lowest value
# Return all four results together.
# Do not use built-in functions that directly calculate the highest, lowest, or total value.
# Test the function with a list of at least five numbers.
numbers = [10,6,7,11,-23,54,34,37,0,-15,-27,100,6.999,-12]
def calculate_statistics(numbers):
    total = 0
    for number in numbers:
        total += number
    numbers.sort()
    highest_value = numbers[-1]    
    lowest_value = numbers[0]    
    average = total / len(numbers)
    results = average, highest_value, lowest_value, total
    return results
#results = calculate_statistics(numbers)
#print(f'[!] The average is: {results[0]:.2f}\n[!] The highest value is: {results[1]:.2f}\n[!] The lowest value is: {results[2]:.2f}\n[!] The total is: {results[3]:.2f}')

# Exercise 3 — Temperature Analysis
# Create a function called analyze_temperatures().
# The function should receive a list of temperatures.
# Determine:
# - the average temperature
# - the highest temperature
# - the lowest temperature
# - how many temperatures are above the average
# Return all four results together.
# Do not use built-in functions that directly calculate → the highest, lowest, or total value.
# Test the function with at least eight temperatures.
# Format the average to two decimal places when displaying it.

temperatures = [18,23,32,27,28,24,34.33333,24.52,26.999,29,32,27,28,24,24.33333,32,27,28,24,34.666]
def analyze_temperatures(temperatures):
    data_copy = temperatures.copy()             # Copiamos la lista para no alterar la entrada de datos original
    data_copy.sort()                            # Ahora ordenamos la lista copiada y trabajamos sobre esta
    lowest, highest = data_copy[0],data_copy[-1]
    total = 0
    above_average = list()
    for each_data in data_copy:
        total += each_data
    average = total / len(data_copy) 
    for temps in data_copy:   
        if temps > average:
            above_average.append(temps)
    results = lowest,highest,average,above_average
    return results

#results = analyze_temperatures(temperatures)
#print(f'[*] The average temperature is: {results[2]:.2f}\n[*] The highest temperature is: {results[1]:.2f}\n[*] The lowest temperature is: {results[0]:.2f}\n[*] The number of temperatures above the average is: {len(results[3])}')

# Exercise 4 — Number Analyzer
# Create a function called analyze_numbers().
# The function should receive a list of numbers.
# Determine:
# - the total
# - the average
# - the highest value
# - the lowest value
# - how many numbers are positive
# - how many numbers are negative
# - how many numbers are zero
# Return all the results together.
# Do not use built-in functions that directly calculate the total, highest, or lowest value.
# Test the function with at least ten numbers.
# Display the average with two decimal places.
numbers = [10,6,7,11,-23,54,34,37,0,-15,-27,100,6.999,-17,0,-15,-27,100,143,24,34.3,43.52,10,6,7,11,-23,54,37,0,-15,-27,100,143,24,34.3,43.52,11,-23,54,37,0,-26,-27,79,11,-23,54,37,0,-85,-27,99,6.999,4,37,0,-35,-27,-70,6.999,-1,-12]
def analyze_numbers(numbers):
    ordered_numbs = numbers.copy()
    ordered_numbs.sort()
    type_of_numbers_counter = {
        'zeros': 0,
        'negatives': 0,
        'positives': 0
    }
    highest_value, lowest_value = ordered_numbs[-1], ordered_numbs[0]
    total = 0
    for number in ordered_numbs:
        total += number
        if number == 0:
            type_of_numbers_counter['zeros'] += 1
        elif number < 0:
            type_of_numbers_counter['negatives'] += 1
        else:
            type_of_numbers_counter['positives'] += 1
    average = total / len(ordered_numbs)
    results = total, average, highest_value, lowest_value, type_of_numbers_counter
    return results
#results = analyze_numbers(numbers)
#print(f"[!] The total is: {results[0]:.2f}\n[!] The average is: {results[1]:.2f}\n[!] The highest value is: {results[2]}\n[!] The lowest value is: {results[3]}\n[!] The quantity of zeros is: {results[4]['zeros']}\n[!] The quantity of positive numbers is: {results[4]['positives']}\n[!] The quantity of negative numbers is: {results[4]['negatives']}")

# Ejercicio 4.1 - Sección de Dalto
# El profesor faltó a clases y los alumnos decidieron armar su propia clase.
# Uno de los alumnos será el profesor y otro será el asistente
# a) Pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor
# b) El mayor de la clase es el profesor y el menor es el asistente. ¿Quién es quién?
# Mi resolución ↓ 
#def pedir_nombres():
#    lista_presentes = {}
#    for i in range(3):
#        nombre = input('Ingrese su nombre: ') 
#        edad = int(input('Ingrese su edad: '))
#        lista_presentes[nombre] = edad
#    return lista_presentes
#presentes = pedir_nombres()
#def profe_y_asis(presentes):
#    datos = list()
#    for nombre,edad in presentes.items():
#        datos.append((edad,nombre))        
#    datos.sort()
#    profesor = datos[-1][1]
#    asistente = datos[0][1]
#    return profesor,asistente
#result = profe_y_asis(presentes)
#print(f"El profesor será: {result[0]} y el asistente será: {result[1]}")

# Resolución de Dalto ↓
#def obtener_compañeros(cantidad_de_compañeros):
#    compañeros = []
#    for i in range(cantidad_de_compañeros):
#        nombre = input("Ingrese el nombre del compañero: ")
#        edad = int(input("Ingrese la edad del compañero: "))
#        compañero = (nombre,edad)
#        compañeros.append(compañero)
#    compañeros.sort(key=lambda x:x[1])
#    asistente = compañero[0][0]
#    profesor = compañero[-1][0]
#    return asistente, profesor
#asistente,profesor = obtener_compañeros(3)
#print(f"El profesor es: {profesor} y su asistente es: {asistente}")

# Ejercicio 4.2 
# Crear una función que nos devuelva los números primos
# Entre 0 y el argumento que le damos

#def get_primes(num):
#    for i in range(2,num-1):
#        if (num%i) == 0: return False
#    return True
#def primes_until(num):
#    primes = []
#    for i in range(3,num+1):
#        result = get_primes(i)
#        if result == True: primes.append(i)
#    return primes
#result = len(primes_until(1000))
#print(result)

# Exercise 5 — Number Distribution
# Create a function called analyze_distribution().
# The function should receive a list of numbers.
# Determine:
# - how many numbers are positive
# - how many numbers are negative
# - how many numbers are zero
# - how many numbers are even
# - how many numbers are odd
# Return all the results together.
# Test the function with at least fifteen numbers,
# including positive, negative, and zero values.
# Do not use built-in functions that directly count
# these categories.
numbers = [4,-3,0,8,-7,2,0,5,-1,6,9,-4,3,0,10,11,-23,54,34,37,0,-15,-27,100,6.999,-17,0,-15,-27,100,143,24]

def analyze_distribution(numbers):
    distribution = {
        'parity': {
            'even': 0,
            'odd': 0
        },
        'sign': {
            'zero': 0,
            'positives': 0,
            'negatives': 0 
        }
    }
    for i in numbers:
        if i == 0:
            distribution['parity']['even'] +=1
            distribution['sign']['zero'] +=1
        elif i%2 == 0:
            distribution['parity']['even'] +=1
            if i > 0:
                distribution['sign']['positives'] +=1
            else:
                distribution['sign']['negatives'] +=1
        else:
            distribution['parity']['odd'] +=1
            if i < 0:
                distribution['sign']['negatives'] +=1
            else:    
                distribution['sign']['positives'] +=1
    return distribution

distribution_results = analyze_distribution(numbers)
print(distribution_results)

