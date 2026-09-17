# Exercise 1: Open a file with a open() 
# open('01_foundations/python/files/data/neuron_signals.txt')

# Exercise 2: Save the result in a variable
file = open('01_foundations/python/files/data/neuron_signals.txt')

# Exercise 3: Read a file with read(), transform a save the result
readed_file = file.read()           # Read devuelve el contenido en este caso como texto plano. 

content = readed_file.split('\n')   # Python conceptualmente recibe "72\n45\n91\n33\n68\n"

#str_to_int = []                     
#for i in content:                   # Vamos a transformar el texto plano en integers.
#    str_to_int.append(int(i))

# Esto que hicimos con open() nos devuelve todo el contenido del archivo, pero a veces puede no ser conveniente.
# Podemos leer línea por línea. Y esto es interesante, ya que el FILE OBJECT ES ITERABLE

# Exercise 4: Read line by line
# file = open('01_foundations/python/files/data/neuron_signals.txt') # Volvemos a abrir el archivo en este caso para no reposicionar el cursor

#for lines in file:                   # Demostramos que el file object es iterable
#    print(lines.strip())             # Agregamos un strip() limpiar el \n de cada línea
    
# Vamos con la escritura de archivos
# Hasta ahora:                   archivo → open() → read() → Procesar datos
# Ahora invertiremos el flujo:   datos → procesar → write() → archivo

# open() en modo lectura
# open(path, 'r') → 'r' = read
# open() en modo escritura
# open(path, 'w') → 'w' = write // → El archivo queda preparado para escritura y su contenido anterior puede ser truncado. 

# Exercise 5 — Write a file
# Create a new text file and write three lines to it using write().

#to_output = open('01_foundations/python/files/data/output.txt','w') # → Abrimos en modo escritura y guardamos
#
#to_output.write("72\n50\ntexto plano")                              # Reemplaza o crea si no está el directorio, por lo que le damos.

# Ahora iremos con append 'a' = append pero aprenderemos withopen tambien
# With open() →
   # Sirve para cerrar el archivo automáticamente al terminar de trabajar

#with open('01_foundations/python/files/data/output.txt', 'a') as output_txt:
#    texto_leido = output_txt.write('\n91') # Como en este caso no queremos sobreescribir, usamos el atributo 'a'
#    # ← Se cierra automáticamente el archivo al salir del bloque.
#with open('01_foundations/python/files/data/output.txt') as output_txt:
#    texto_leido = output_txt.read()        # Leemos el archivo y guardamos
#    print(texto_leido)
    # ← Se cierra automáticamente el archivo al salir del bloque.

# Exercise 6 — Read → Transform → Write
# Read neuron_signals.txt and: 
    # Read the file.
    # Obtain the values as int.
    # Calculate the average.
    # Create o write a new file average.txt.
    # Save the output there.

with open('01_foundations/python/files/data/neuron_signals.txt', 'r') as neuron_signals:
    neuron_signals_file = neuron_signals.read()
    neuron_list = neuron_signals_file.split('\n')
    signals = []
    for signal in neuron_list:
        signal_int = int(signal.strip())
        signals.append(signal_int)
    signals_average = sum(signals) / len(signals)
    print(signals_average)

with open('01_foundations/python/files/data/average.txt', 'w', encoding="UTF-8") as average_file:
    average = str(signals_average)
    average_file.write(average)
    