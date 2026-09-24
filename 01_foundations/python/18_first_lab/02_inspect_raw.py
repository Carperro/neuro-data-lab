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
    
file_path = ('01_foundations/python/18_first_lab/''data/sleep/raw/SN007_sleepscoring.txt')

with open(file_path, 'r', encoding='UTF-8') as patient_data:
    # 1. Leemos el archivo todo como un solo string.
    patient_results = patient_data.read()

    # 2. Inspeccionamos la estructura general del contenido
    
        # Count total characters.
    n_characters = len(patient_results)

        # Separate the raw file into individual lines.
    result_lines = patient_results.split('\n')
    
        # Extract and split the first line into column names.
    header_row = result_lines[0].split(',')
    
        # Define the expected number of columns.
    expected_columns = len(header_row)
    
        # Count total lines, including the header.
    total_rows = len(result_lines)

    # 3. STORAGE STRUCTURES

    rows_complete_fields = 0
    rows_w_empty_field = 0
        # Stores rows whose number of columns differs from the expected number.
    rows_w_anomalies = {}
        # Stores the raw values grouped by column.
    columns = {}
        # Stores information about rows containing blank fields.
    empty_field_description = {}
        # Stores distinct raw values for each column.
    unique_values = {}
        # Stores the number of distinct values per column.
    unique_counts = {}

    # Create storage for every column.
    for header in header_row:
        columns[header] = []
        unique_values[header] = set()

    # 4. ROW STRUCTURE + COLUMN STORAGE

    for index, line in enumerate(result_lines[1:], start=1):
        line_in_list = line.split(',')
        # Convert the current raw line into a list of fields.
        column_count = len(line_in_list)

        # Check structural consistency

        if column_count != expected_columns:
            rows_w_anomalies[index] = {
                'line_number': index,
                'expected_columns': expected_columns,
                'actual_columns': column_count,
                'raw_line': line
            }

        # Check blank fields

        if " " in line_in_list:

            rows_w_empty_field += 1

            empty_index = line_in_list.index(" ")

            empty_field_description[index] = {
                'line_number': index,
                'empty_slot': empty_index,
                'column': header_row[empty_index]
            }
        else:
            rows_complete_fields += 1

        # Store values by column
        for header, value in zip(header_row, line_in_list):
            columns[header].append(value)

    # 5. UNIQUE VALUES

    for header in header_row:
        for value in columns[header]:
            unique_values[header].add(value)
    # Count distinct values per column.
    for header, values in unique_values.items():
        unique_counts[header] = len(values)

    # 6. FREQUENCY COUNTS

    # Duration frequencies
    duration_counts = {}

    for duration in columns[' Duration']:
        if duration not in duration_counts:
            duration_counts[duration] = 1
        else:
            duration_counts[duration] += 1

    # Annotation frequencies

    annotation_counts = {}
    for annotation in columns[' Annotation']:
        if annotation not in annotation_counts:
            annotation_counts[annotation] = 1
        else:
            annotation_counts[annotation] += 1

    # Linked channel frequencies
    linked_channel_counts = {}

    for linked_channel in columns[' Linked channel']:
        if linked_channel not in linked_channel_counts:
            linked_channel_counts[linked_channel] = 1
        else:
            linked_channel_counts[linked_channel] += 1

    # 7. RECORDING ONSET — NUMERIC VALIDATION + RANGE

    rec_onset_values = {}

    for index, recording_onset in enumerate(columns[' Recording onset']):
        try:
            value_to_float = float(recording_onset)
            # Initialize min/max with the first valid value.
            if index == 0:
                rec_onset_values['min'] = value_to_float
                rec_onset_values['max'] = value_to_float
            # Update maximum.
            if value_to_float > rec_onset_values['max']:
                rec_onset_values['max'] = value_to_float
            # Update minimum.
            if value_to_float < rec_onset_values['min']:
                rec_onset_values['min'] = value_to_float
        except ValueError:
            print(f'Data → {recording_onset}')
            # Report values that cannot be converted to float.

    # 8. DURATION — NUMERIC VALIDATION + RANGE

    duration_values = {}

    for index, duration in enumerate(columns[' Duration']):
        try:
            duration_value = int(duration)

            # Initialize min/max with the first valid value.
            if index == 0:
                duration_values['min'] = duration_value
                duration_values['max'] = duration_value

            # Update maximum.
            if duration_value > duration_values['max']:
                duration_values['max'] = duration_value

            # Update minimum.
            if duration_value < duration_values['min']:
                duration_values['min'] = duration_value

        except ValueError:
            print(f'Data → {duration}')
            # Report values that cannot be converted to int.

    # 9. TIME — STRUCTURAL PATTERNS

    time_element_counts = {}

    for time_value in columns[' Time']:
        time_element_format = time_value.split('.')
        component_count = len(time_element_format)
        if component_count not in time_element_counts:
            time_element_counts[component_count] = 1
        else:
            time_element_counts[component_count] += 1

    # Inspect Time values containing four components.
    for (time_value,line,recording_onset_value) in zip(columns[' Time'],result_lines[1:],columns[' Recording onset']):
        time_element_format = time_value.split('.')
        if len(time_element_format) == 4:
            print(f'Line complete: {line}\n'f'Time value: {time_element_format}\n'f'Recording onset: {recording_onset_value}')

    # 10. DATE — STRUCTURAL PATTERNS

    date_element_counts = {}
    for date in columns['Date']:
        date_element_format = date.split('.')
        n_elements_date = len(date_element_format)
        if n_elements_date in date_element_counts:
            date_element_counts[n_elements_date] += 1
        else:
            date_element_counts[n_elements_date] = 1

    # 11. EMPTY VALUES

    empty_values = {}
    for header, values in columns.items():
        for value in values:
            if value.strip() == '':
                if header not in empty_values:
                    empty_values[header] = 1
                else:
                    empty_values[header] += 1

    # 12. CROSS-COLUMN CHECKS

    # Check records with Duration = 0.
    for annotation, duration in zip(columns[' Annotation'],columns[' Duration']):
        if duration == ' 0':
            print(f'Value: {annotation}\n'f'Duration: {duration}')

    # Check records associated with SaO2.
    for annotation, duration, linked_channel in zip(
        columns[' Annotation'],
        columns[' Duration'],
        columns[' Linked channel']
    ):
        if linked_channel == ' SaO2':
            print(
                f'Value: {annotation}\n'
                f'Duration: {duration}\n'
                f'Linked channel: {linked_channel}'
            )


# ================================================================
# 13. BASIC INSPECTION OUTPUT
# ================================================================

print('\n--- BASIC STRUCTURE ---')
print(f'Characters: {n_characters}')
print(f'Total lines: {total_rows}')
print(f'Header: {header_row}')
print(f'Expected columns: {expected_columns}')
print('\n--- UNIQUE VALUES ---')
print(unique_counts)
print('\n--- DURATION FREQUENCIES ---')
print(duration_counts)
print('\n--- ANNOTATION FREQUENCIES ---')
print(annotation_counts)
print('\n--- LINKED CHANNEL FREQUENCIES ---')
print(linked_channel_counts)
print('\n--- RECORDING ONSET ---')
print(f'Recording onset min: 'f'{rec_onset_values["min"]}')
print(f'Recording onset max: 'f'{rec_onset_values["max"]}')
print('\n--- DURATION RANGE ---')
print(f'Duration min: 'f'{duration_values["min"]}')
print(f'Duration max: 'f'{duration_values["max"]}')
print('\n--- TIME STRUCTURE ---')
print(time_element_counts)
print('\n--- DATE STRUCTURE ---')
print(date_element_counts)
print('\n--- EMPTY VALUES ---')
print(empty_values)
print('\n--- STRUCTURAL ANOMALIES ---')
print(rows_w_anomalies)


    
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