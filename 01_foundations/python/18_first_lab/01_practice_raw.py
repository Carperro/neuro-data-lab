# TASK
# 1. Open SN007_sleepscoring with `with open()`.
# 2. Read the entire file.
# 3. Print the result.
# 4. Print its Python type.

# with open('data/sleep/raw/SN007_sleepscoring.txt','r',encoding='UTF-8') as sleep_data:
#     sleep_content = sleep_data.read()
#     print(sleep_content)

# TASK 2
#1. Separate the content into lines.
#2. Store the result in a variable.
#3. Print the resulting object.
#4. Print its type.
#5. Print its length.

# TASK 3 — Discover annotation categories

    #print(len(header))
    #print(len(first_row))
    #print(header)
    #print(first_row)

#import os
#print("CWD:", os.getcwd())

#file_path = '01_foundations/python/18_first_lab/data/sleep/raw/SN007_sleepscoring.txt'
#print("Exists:", os.path.exists(file_path))

with open('01_foundations/python/18_first_lab/data/sleep/raw/SN007_sleepscoring.txt', 'r', encoding='UTF-8') as sleep_data:
    sleep_content = sleep_data.read()           # Leemos todo el archivo y lo almacenamos como str
    content_list = sleep_content.split('\n')    # Separamos el contenido por \n para obtener una lista de líneas

# Tests:
# print(type(sleep_content))                   # Comprobamos que sleep_content sea str
# print(type(content_list))                    # Comprobamos que content_list sea list
# print(len(content_list))                     # Comprobamos la cantidad de líneas
# print(content_list[0])                        # Mostramos el header
# print(content_list[1])                        # Mostramos la primera fila de datos
    
  # annotation_values = set()                   # Set donde almacenaremos los valores únicos de Annotation
    header = content_list[0].split(',')         # Separamos el header por ',' para obtener los nombres de las columnas
    first_row = content_list[1].split(',')      # Separamos la primera fila de datos por ','
    rows = []                                   # Lista donde almacenaremos cada fila como un diccionario
    for row in content_list[1:]:                # Recorremos todas las filas de datos, excluyendo el header
        only_row = row.split(',')               # Separamos la fila actual en sus distintos valores
        if len(only_row) != 6:                  # Comprobamos que la fila tenga exactamente 6 columnas
            print(f'Quantity: {len(only_row)}\nRow: {row}')  # Mostramos las filas que no tengan 6 columnas
        row_data = {}                           # Creamos un diccionario para representar la fila actual
        for column_name, value in zip(header, only_row):    # Emparejamos cada nombre de columna con su valor correspondiente
            row_data[column_name] = value                    # Guardamos cada par column_name → value en el diccionario
        rows.append(row_data)                   # Agregamos el diccionario completo a la lista de filas

# Step 4 — Profile the columns

    duration_values = []               # Lista donde almacenaremos los valores de Duration
    rec_onset_values = set()              # Lista donde almacenaremos los valores de Recording onset
    dates_values = []                  # Lista donde almacenaremos los valores de Date
    annotation_values = []             # Lista donde almacenaremos los valores de Annotation
    linked_channel_values = []         # Lista donde almacenaremos los valores de Linked channel
    duration_counts = {}               # Diccionario donde contaremos las apariciones de cada valor de Duration
    for row in rows:                            # Recorremos cada diccionario almacenado en rows
        duration_values.append(row[" Duration"])                # Extraemos Duration y lo agregamos a la lista
        rec_onset_values.add(row[" Recording onset"])           # Extraemos Recording onset y lo agregamos a la lista
        dates_values.append(row["Date"])                        # Extraemos Date y lo agregamos a la lista
        annotation_values.append(row[" Annotation"])            # Extraemos Annotation y lo agregamos a la lista
        linked_channel_values.append(row[" Linked channel"])    # Extraemos Linked channel y lo agregamos a la lista
    for value in duration_values:               # Recorremos cada valor almacenado en duration_values
        if value not in duration_counts:        # Comprobamos si el valor todavía no existe en el diccionario
            duration_counts[value] = 0          # Si no existe, lo inicializamos en cero
        duration_counts[value] += 1             # Sumamos una aparición del valor actual
    test = 0
    for value in rec_onset_values:
        print(value)
        test += 1
        if test == 10:
            break 


    # print(len(rec_onset_values))                      # Mostramos la cantidad de apariciones de cada valor de Duration
    
# Siguiente columna: Recording onset
   