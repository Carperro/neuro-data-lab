# ¿Qué es un dictionary?
# Un dictionary es una estructura de datos que almacena pares key → value.
diccionario = {
    'key': 'value de la key 1',
    'key_2': True,
    'version': 1.0
}

# ¿Cómo lo creo?
# Se puede crear como en el ejemplo anterior, pero también tenemos la funcion dict(), al igual que list(), tuple() → Son funciones built-in de python
    # dict(), list() y tuple() son built-in classes/types.
    # Pueden utilizarse para crear nuevas estructuras de datos..
dictionary_2 = dict() # Es lo mismo que → dictionary = {} ← De hecho es mas habitual esta manera

# ¿Cómo agrego una key?
diccionario['adding_a_key'] = "Agregando key al ejemplo 1" # → Puede agregar una nueva key o sobrescribir el value si esa key ya existe.
diccionario['objeto_para_eliminar'] = "Método pop()"
print(diccionario)

# ¿Cómo accedo a un value?
    # Los dictionaries no utilizan índices numéricos como las listas.
    # Accedemos a los values mediante sus keys.
key_obtaining = diccionario['version'] # → busca la key 'version' y devuelve su value 1.0.
print(key_obtaining)

# ¿Cómo modifico un value?
# Podemos modificar un value llamando a la key y reasignando su valor
diccionario['version'] = 1.1
print(diccionario) # → Notemos que paso de 1.0 a 1.1

# ¿Cómo elimino una key?
# Se puede eliminar una key con el método pop() y como parámetro pasamos el key.
diccionario.pop("objeto_para_eliminar")
print(diccionario)

# ¿Cómo sé cuántos elementos tiene?
# Podemos obtener la longitud usando la función len()
longitud = len(diccionario)                 # → len(dictionary) → Devuelve la cantidad de key-values pairs. 
print(f'El diccionario contiene {longitud} elementos en formato key → value.')

# ¿Cómo lo recorro?
# Podemos recorrerlo con un bucle for.
for key,value in diccionario.items(): # → En este caso recorremos keys y values de a pares, pero se puede hacer por uno u otro según mpetodo
    print(f'Key: [!] {key} y Value: [!] {value} de la entrada')

# ¿Qué hacen keys(), values(), items()?
# Son 3 métodos de diccionario. Los métodos permiten manipular y consultar estructuras key → value
    # keys() → Devuelve las key del diccionario
keys_method = diccionario.keys()
print(f'[!] Devolviendo keys → {keys_method}')

    # values() → Devuelve los valores del diccionario
values_method = diccionario.values()
print(f'[!] Devolviendo values → {values_method}')

    # items() → Devuelve los pares key/value del diccionario
items_method = diccionario.items()
print(f'[!] Devolviendo pares key/value → {items_method}')

# ¿Cómo compruebo si existe una key?
# Podemos utilizar el operador in para comprobar si una key existe en el dictionary.

if 'This_key_exist?' in diccionario:
    print("Esta key existe")
else:
    print("Esta key no existe")

# ¿Cómo trabajo con un dictionary dentro de otro?
# Hagamos un ejercicio de ejemplo:
    # Crearemos un diccionario llamado neural_population que va a contener la información de 3 neuronas.
    # Cada neurona debe tener: neuron_type; firing_rate; signal_strength
    # Luego haremos un print del diccionario completo
    # Haremos un acceso y un print de neuron_type de la neuron_2
    # Cambiaremos la signal_strength de la neuron_3
    # Y añadiremos un nuevo campo 'status' a la neuron_1
    # E imprimiremos por completo el diccionario nuevamente
# 1 - Creamos el primer diccionario:    
neural_population = {
    'neuron_1' : {
        'neuron_type': 'inhibitory',
        'firing_rate': 80,
        'signal_strength': 40
    },
    'neuron_2' : {
        'neuron_type': 'excitatory',
        'firing_rate': 60,
        'signal_strength': 70
    },
    'neuron_3' : {
        'neuron_type': 'motor',
        'firing_rate': 50,
        'signal_strength': 65
    }
}
# 2 - Lo imprimimos por completo
print(neural_population) 
# 3 - Accedemos y hacemos un print del neuron_type de la neurona 2
print(f"[+] Imprimiendo el neuron_type de la neurona 2: {neural_population['neuron_2']['neuron_type']}") # → Hacemos un doble acceso, primero al diccionario 'general' luego al que esta dentro. En ambos casos llamamos por la key, y obtenemos su value.
# 4 - Cambiamos la signal_strength de la neurona 3
neural_population['neuron_3']['signal_strength'] = 100
# 5 - Añadimos un nuevo campo 'status' a la neurona 1
neural_population['neuron_1']['status'] = 'strong'
# 6 - Imprimimos nuevamente el diccionario completo
print(neural_population)
# Los datos del diccionario, en cuanto a value, puede tener todo timo de datos. Pero en cuanto a keys, debe ser requisito que sea hasheable. 

# ¿Cómo uso get()? 
# get() → obtiene el value asociado a una key
print(neural_population.get('neuron_1')) # En este caso retornara un diccionario
print(diccionario.get('version')) # En este caso retornara el valor de version del primer diccionario. (1.1)

# ¿Qué diferencia hay entre dictionary[key] y dictionary.get(key)?
# La diferencia es que dictionary[key] → 
# Y el método: dictionary.get(key) → 
print(neural_population['neuron_1']) # → → Acceso directo al value asociado a la key.
                                     # → Si la key no existe, produce KeyError.
                                     
print(neural_population.get('neuron_99',"This key doesn't exist"))  # → Intenta obtener el value asociado a la key.
                                                                    # → Si no existe, devuelve None.
                                                                    # → Podemos indicar un valor alternativo.
                                             
# ¿Cómo puedo actualizar varios valores?
# Un ejemplo lo mostraría mejor, porque tenemos varias formas. 
# Exercise - Update Neural Data
# Partimos de ↓ 
neuron = {
    "neuron_type": "excitatory",
    "firing_rate": 60,
    "signal_strength": 45,
    "status": "weak"
}
print(neuron)

# Ahora queremos actualizar 3 valores
neuron['neuron_type'] = 'inhibitory'
neuron['firing_rate'] = 90
neuron['signal_strength'] = 70      # Esto es la forma más clara y directa cuando sabemos exactamente qué keys queremos modificar.
print(neuron)

# Pero también existe un método que hace esto un poco más fácil → update()
# Este método permite hacer varias modificaciones de una sola vez ↓ 
neuron.update({                             # Hace varias operaciones de tipo: dictionary[key] = value → De una sola vez
    "neuron_type": "inhibitory",
    "firing_rate": 80,
    "signal_strength": 105,
    "status": "Strong"
})
print(neuron)

# En otros casos podríamos utilizar un bucle for
# Por ejemplo, si tuvieramos: ↓
neural_population = {
    'neuron_1' : {
        'neuron_type': 'inhibitory',
        'firing_rate': 80,
        'signal_strength': 40
    },
    'neuron_2' : {
        'neuron_type': 'excitatory',
        'firing_rate': 60,
        'signal_strength': 70
    },
    'neuron_3' : {
        'neuron_type': 'motor',
        'firing_rate': 50,
        'signal_strength': 65
    }
}
# Y quisieramos cambiar el 'firing_rate' de todas: 
for neurons in neural_population:
    (neural_population[neurons]['firing_rate']) += 10 # Accedo al value de firing_rate en cada neurona 
    
print(neural_population)
    
# ¿Cómo puedo limpiar un dictionary?
# Para limpiar un diccionario podemos usar la función .clear(), esto vaciará el diccionario por completo
vaciame = {
    'key_1' : 'borrame',
    'key_2' : True,
    'key_3' : 30
} # → Creamos el diccionario
print(vaciame)      # → Mostramos el contenido
vaciame.clear()     # → Usamos la función clear para limpiarlo, borra las entradas de key/value, no el objeto diccionario
print(vaciame)      # → Vemos que ya se encuentra vacío

# ¿Cómo puedo crear una copia de un dictionary?
# Podemos usar el método .copy(), que crea un nuevo dictionary
# con los mismos key-value pairs que el original.
original = {
    'key_1': 'value_1',
    'key_2': True,
    'key_3': 30
}  # → Creamos el dictionary original
copied = original.copy()  # → Creamos una copia del dictionary
print(original)  # → Mostramos el dictionary original
print(copied)    # → Mostramos la copia
copied['key_1'] = 'changed'  # → Modificamos un value de la copia
print(original)  # → El dictionary original no cambia
print(copied)    # → La copia contiene el nuevo value