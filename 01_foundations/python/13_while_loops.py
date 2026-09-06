# Exercise 1 — Neural countdown
# Create a program that starts with a positive integer.
# While the number is greater than zero:
# - display the current number
# - decrease the number by one
# Stop when the number reaches zero.
# Test the program with different starting values.

#i = 10
#while i > 0:
#    print(i)
#    i -= 1
    
# Exercise 2 — Neural signal accumulation
# Create a program that starts with a signal strength of 0.
# While the signal strength is below 100:
# - increase the signal strength by 10
# - display the current signal strength
# Stop when the signal strength reaches 100.
# Test the program with different starting values.
#signal_strength = 0
#while signal_strength < 100:
#    signal_strength += 10
#    print(signal_strength) 

# Exercise 3 — Neuron threshold
# Create a program that starts with a membrane potential
# below the action potential threshold.
# While the membrane potential is below the threshold:
# - increase the membrane potential
# - display its current value
# Stop when the membrane potential reaches the threshold.
# Use a threshold of -55.
# Use a starting membrane potential below the threshold.
# Choose the increase yourself.

#membrane_potential = -90
#threshold = -55
#
#while membrane_potential < threshold:
#    membrane_potential += 5
#    print(f'The current value is: {membrane_potential}')

# Exercise 4 — Neural monitoring
# Create a program that repeatedly asks the user to enter a membrane potential.
# Continue asking for values while the user enters a value below the threshold.
# Stop when the user enters a value that reaches or exceeds the threshold.
# Use a threshold of -55.
# Display a message when the threshold is reached.
threshold = -55
#membrane_potential = int(input('Enter a initial membrane potential: '))

#while membrane_potential < threshold:
#    new_value = int(input('Enter a new membrane potential: '))
#    if new_value == threshold:
#        print('Threshold has been reached')
#        break
#    elif new_value > threshold:
#        break
#    membrane_potential = new_value
        
# Exercise 5 — Neural firing counter
# Create a program that repeatedly asks the user to enter a firing rate.
# Continue asking for values while the firing rate is below 50.
# Count how many values were entered before the firing rate reached or exceeded 50.
# Display the total number of values entered.
# Test the program with different sequences of values.

#firing_rate = int(input('Enter a initial firing rate: '))
#counter_values = 0
#while firing_rate < 50:
#    counter_values += 1
#    new_firing_rate = int(input('Enter a new firing rate: '))
#    firing_rate = new_firing_rate
#    if new_firing_rate >= 50:
#        print(f'Values entered until the firing rate reached or exceeded: {counter_values + 1}')
#        break
    
# Exercise 6 — Neural signal filtering
# Create a program that repeatedly asks the user to enter a signal strength.
# If the value is negative:
# - ignore it
# - continue asking for another value
# If the value is zero or positive:
# - display the value
# Stop when the user enters a signal strength greater than 100.
# Test the program with negative, valid, and threshold-exceeding values.    

#signal_strength = int(input('Enter a signal strentgh: '))
#while True:
#    if signal_strength < 0:
#        new_signal = int(input('Enter a new signal strentgh: '))
#        signal_strength = new_signal
#        continue    
#    elif signal_strength > 100:
#        break
#    else: 
#        new_signal = int(input('Enter a new signal strentgh: '))
#        signal_strength = new_signal
#        print(signal_strength)

# Exercise 7 — Neural Signal Analysis
# Create a program that repeatedly asks the user to enter a signal strength.
# If the signal strength is negative:
# - ignore the value
# - continue asking for another value
# If the signal strength is between 0 and 100:
# - count the value
# - continue asking
# If the signal strength is greater than 100:
# - stop the program
# At the end, display how many valid signal were entered.
# Test the program with negative, valid,
# and threshold-exceeding values.

#signal_strength = int(input('Enter a signal strentgh: '))
#values = 0
#while True:
#    if signal_strength < 0:
#        signal_strength = int(input('Enter a new signal strength: '))
#        continue
#    if 0 <= signal_strength <= 100:
#        values += 1
#        signal_strength = int(input('Enter a new signal strength: '))
#    else:
#        break
#print(values)

# Exercise 8 — Neural Signal Statistics
# Create a program that repeatedly asks the user to enter a signal strength.
# Ignore negative values.
# For values from 0 to 100:
# - count the value
# - add the value to a total
# Stop when the user enters a value greater than 100.
# At the end, display:
# - the number of valid values entered
# - the total of all valid values
# If no valid values were entered, handle that case appropriately.
# Test the program with different sequences of values.

#valid_signals = list()
#while True:
#    signal_strength = int(input('Enter a signal strentgh: '))
#    if signal_strength < 0:
#        continue
#    if 0 <= signal_strength <= 100:
#        valid_signals.append(signal_strength)
#    else:
#        break
#print(f"[!] The total of all values is: {sum(valid_signals)}\n[!] The total of values entered is: {len(valid_signals)}")

# Exercise 9 — Neural Data Collection
# Create a program that repeatedly asks the user to enter a neuron type.
# Valid neuron types are:
# - excitatory
# - inhibitory
# - sensory
# If the user enters a valid neuron type:
# - count it
# - continue collecting data
# If the user enters anything else:
# - stop the program
# At the end, display how many valid neuron types were entered.
# Test the program with different sequences, including repeated neuron types.

#classified_neurons = {
#    'excitatory': 0,
#    'inhibitory': 0,
#    'sensory': 0
#}
#valid_neurons = ('excitatory','inhibitory','sensory')
#while True: 
#    neuron_type = input('Enter a neuron type: ').lower()
#    if neuron_type in valid_neurons:
#        classified_neurons[neuron_type] += 1
#        continue
#    else:
#        break
#total = sum(classified_neurons.values())
#print(total)

# Exercise 10 — Neural Population Monitor
# Create a program that repeatedly asks the user to enter a neuron type and a signal strength.
# Valid neuron types are: excitatory, inhibitory, sensory
# For each entry:
# - ignore the entry if the signal strength is negative
# - count the neuron if the type is valid and the - signal strength is between 0 and 100
# Stop the program when the user enters a signal strength greater than 100.
# At the end, display:
# - the number of valid neurons
# - the number of excitatory neurons
# - the number of inhibitory neurons
# - the number of sensory neurons
# Test the program with repeated neuron types, negative signal strengths, and a value greater than 100.

neurons_counter = {
    'excitatory': 0,
    'inhibitory': 0,
    'sensory': 0
}
valid_neurons = ('excitatory','inhibitory','sensory')

while True:
    signal_strength = int(input('Enter a signal strength: '))
    neuron_type = input('Enter a neuron type: ').lower()
    if signal_strength < 0:                       
        continue
    if neuron_type in valid_neurons: 
        if 0 <= signal_strength <= 100:
            neurons_counter[neuron_type] += 1
        else:
            continue
    if signal_strength > 100:
        break
            
total_valid_neurons = sum(neurons_counter.values()) # → La unica duda que tengo es la identación de esta variable, creo que debería estar por fuera del while.
print(f"""
      [*] Total of valid neurons = {total_valid_neurons} 
      [*] Total of excitatory neurons = {neurons_counter['excitatory']} 
      [*] Total of inhibitory neurons = {neurons_counter['inhibitory']} 
      [*] Total of sensory neurons = {neurons_counter['sensory']} 
      """)
    