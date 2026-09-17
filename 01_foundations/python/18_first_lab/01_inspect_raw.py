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

# import os
# print(os.getcwd()) # → Vemos desde donde está buscando python

with open('data/sleep/raw/SN007_sleepscoring.txt','r',encoding='UTF-8') as sleep_data: # Abrimos en modo read, encoding y as para manipularlo luego.
    sleep_content = sleep_data.read()           # Leemos el archivo y guardamos su respuesta
    content_list = sleep_content.split('\n')    # Nos devuelve una lista separa en función de: \n
    
    # Comprobamos:
        # print(type(content_list))                   # Comprobamos el tipo de dato, efectivamente es una lista
        # print(len(content_list))                    # Medimos la longitud, vemos que cuenta por linea como unidad, cada linea es una longitud.
        # print(content_list[0])                      # Para esta DB → "Date, Time, Recording onset, Duration, Annotation, Linked channel"
    

    content_list_cleaned = content_list[0].split(',')
    def data_cleaner(content_list_cleaned):
        content_lines = []
        for i in content_list_cleaned:
            i_clean = i.strip()
            content_lines.append(i_clean)
            
#        print(content_lines[0])
#        print(content_lines)
#        print(content_list[1])
        
        return content_lines
    result = data_cleaner(content_list_cleaned)
    print(result)
            
    
    


        