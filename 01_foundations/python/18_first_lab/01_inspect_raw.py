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
    sleep_content = sleep_data.read()           # Leemos el archivo y lo almacenamos
    content_list = sleep_content.split('\n')    # Cortamos el output de read() por los \n para obtener una lista por cada linea
# Tests: 
# print(type(sleep_content)) // print(type(content_list)) // print(len(content_list)) // print(content_list[0]) // print(content_list[1])
    header = content_list[0].split(',')         # Separamos el header por ',' para obtener los nombres de las columnas
    first_row = content_list[1].split(',')      # Separamos la primera fila de datos por ','
    annotation_values = set()                   # Set donde almacenamos los valores únicos de Annotation
    rows = []                                   # Lista donde almacenaremos cada fila como un diccionario
    for row in content_list[1:]:                # Recorremos todas las filas de datos, excluyendo el header
        only_row = row.split(',')               # Separamos la fila actual en sus distintos valores
        if len(only_row) != 6:                  # Comprobamos que la fila tenga exactamente 6 columnas
            print(f'Quantity: {len(only_row)}\nRow: {row}')     # Mostramos las filas que no tengan 6 columnas
        row_data = {}                           # Creamos un diccionario para representar la fila actual
        for column_name,value in zip(header,only_row):          # Emparejamos cada nombre de columna con su valor correspondiente
            row_data[column_name] = value       # Guardamos cada par column_name → value en el diccionario
        rows.append(row_data)                   # Agregamos el diccionario completo a la lista de filas

# Step 4 — Profile the columns
    duration_values = []                            
    rec_onset_values = []                            
    dates_values = []                            
    times_values = []                            
    annotation_values = []                            
    linked_channel_values = []                            
    duration_counts = {}
    for row in rows:                                # Recorremos cada diccionario almacenado en rows
        duration_values.append(row[" Duration"])    # Extraemos el valor de duration_values y lo agregamos a la lista
        rec_onset_values.append(row[" Recording onset"])    # Extraemos el valor de rec_onset_values y lo agregamos a la lista
        dates_values.append(row["Date"])
        times_values.append(row[" Time"])
        annotation_values.append(row[" Annotation"])
        linked_channel_values.append(row[" Linked channel"])
    print(rec_onset_values)                         # OJO: row no corresponde necesariamente al value actual; quedó de un for anterior
    for value in duration_values:                   # Recorremos cada valor almacenado en duration_values
        if value not in duration_counts:            # Detectamos los valores de Duration que sean diferentes de 30
            duration_counts[value] = 0                              
            duration_counts[value] += 1                             
        else:
            duration_counts[value] += 1   
    print(duration_counts)                         # Mostramos todos los valores de duration_counts para inspeccionarlos
            
# Siguiente columna: Recording onset
    