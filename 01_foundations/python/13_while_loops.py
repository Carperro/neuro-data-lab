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

membrane_potential = -90
threshold = -55

while membrane_potential < threshold:
    membrane_potential += 5
    print(f'The current value is: {membrane_potential}')

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

firing_rate = int(input('Enter a initial firing rate: '))
counter_values = 0
while firing_rate < 50:
    counter_values += 1
    new_firing_rate = int(input('Enter a new firing rate: '))
    firing_rate = new_firing_rate
    if new_firing_rate >= 50:
        print(f'Values entered until the firing rate reached or exceeded: {counter_values + 1}')
        break
    
# Exercise 6 — Neural signal filtering
# Create a program that repeatedly asks the user to enter a signal strength.
# If the value is negative:
# - ignore it
# - continue asking for another value
# If the value is zero or positive:
# - display the value
# Stop when the user enters a signal strength greater than 100.
# Test the program with negative, valid, and threshold-exceeding values.    

signal_strength = int(input('Enter a signal strentgh: '))
while True:
    if signal_strength < 0:
        new_signal = int(input('Enter a new signal strentgh: '))
        signal_strength = new_signal
        continue    
    elif signal_strength > 100:
        break
    else: 
        new_signal = int(input('Enter a new signal strentgh: '))
        signal_strength = new_signal
        print(signal_strength)
    