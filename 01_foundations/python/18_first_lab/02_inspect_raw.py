# Recibimos bases de datos de un estudio y debemos trabajarlos para devolverlos al laboratorio. 
# Si bien son formato CSV. Piden hacerlo manualmente desde un .txt.
# Deberé crear todo el sistema manualmente. Sin librerías.
# Modularizar el tratamiento ya que se van a recibir muchos más documentos de estos. 
# El documento es un registro de sueños de cada paciente. 
# Documentar los pasos que hace el código para mayor legibilidad. 
# Este documento funcionará para responder las siguientes preguntas:
    # ¿Tiene header?
    # ¿Cuántas líneas?
    # ¿Cuántas columnas?
    # ¿Todas las filas tienen la misma estructura?
    # ¿Qué valores aparecen?
    # ¿Qué campos están vacíos?
    # ¿Qué patrones tienen los valores?
    # ¿Qué tipos de datos parecen representar?
    # ¿Hay anomalías?
with open('01_foundations/python/18_first_lab/data/sleep/raw/SN007_sleepscoring.txt', 'r', encoding='UTF-8') as patient_data:
    patient_results = patient_data.read()
    
    n_characters = len(patient_results)
    result_lines = patient_results.split('\n')
    header_row = result_lines[0].split(',')
    expected_columns = len(header_row)
    total_rows = len(result_lines)
    
    rows_complete_fields = 0
    rows_w_empty_field = 0
    rows_w_anomalies = {}
    columns = {}
    empty_field_description = {}
    unique_values = {}
    unique_counts = {}
    
    # Create the structure for each column
    for header in header_row:
        columns[header] = []
        unique_values[header] = set()
        
    # Inspect and collect each row
    for index, line in enumerate(result_lines[1:], start=1):
        line_in_list = line.split(',')
        column_count = len(line_in_list)

        if column_count != expected_columns:
            rows_w_anomalies[index] = {'line_number': index,'expected_columns': expected_columns,'actual_columns': column_count,'raw_line': line}
        if " " in line_in_list:
            rows_w_empty_field += 1
            empty_index = line_in_list.index(" ")
            empty_field_description[index] = {'line_number': index,'empty_slot': empty_index,'column': header_row[empty_index]}
        else:
            rows_complete_fields += 1

        for header, value in zip(header_row, line_in_list):
            columns[header].append(value)

    # Find unique values for each column
    for header in header_row:
        for value in columns[header]:
            unique_values[header].add(value)

    # Count unique values for each column
    for header, values in unique_values.items():
        uniq_values_column = len(values)
        unique_counts[header] = uniq_values_column
    
    duration_counts = {} 
    for i in columns[' Duration']:
        if i not in duration_counts:
            duration_counts[i] = 1
        else: 
            duration_counts[i] += 1
    annotation_counts = {} 
    for i in columns[' Annotation']:
        if i not in annotation_counts:
            annotation_counts[i] = 1
        else: 
            annotation_counts[i] += 1
            
    linked_channel_counts = {} 
    for i in columns[' Linked channel']:
        if i not in linked_channel_counts:
            linked_channel_counts[i] = 1
        else: 
            linked_channel_counts[i] += 1
            
    for value, duration, link_channel in zip(columns[' Annotation'], columns[' Duration'], columns[' Linked channel']):
        if link_channel == ' SaO2':
            print(f'Value: {value}\nDuration: {duration}\nLinked channel: {link_channel}')
    
    for index, data in enumerate(columns[' Recording onset']):
        try:
            columns_converted = float(data)
        except ValueError:
            print(f'Data → {data}\nIndex → {index}')
            
        
    
    
    
# representation = print(f"""
# ========== RAW DATA INSPECTION ==========

# FILE
# Path: 01_foundations/python/18_first_lab/data/sleep/raw/SN007_sleepscoring.txt
# Encoding: UTF-8
# Characters: {n_characters}
# Lines: {total_rows}

# STRUCTURE
# Header: Yes
# Delimiter:
# Columns: {column_count}
# Rows: {total_rows} 

# INTEGRITY
# Rows complete: {rows_complete_fields}
# Rows with empty fields: {rows_w_empty_field}
# Rows with invalid column count: {rows_w_anomalies}

# COLUMNS
# 0 → Date
# 1 → Time
# 2 → Recording onset
# 3 → Duration
# 4 → Annotation
# 5 → Linked channel

# VALUES
# Date: 
# Time:
# Recording onset:
# Duration:
# Annotation:
# Linked channel:

# ==========================================
# """)