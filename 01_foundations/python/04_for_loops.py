# Python loops 
# A loops allows us yo repeat a block of code multiple times
# In this file, we will learn how to use 'for' loops and the range() function

# La esctructura: 
# Un 'for' básico tiene la siguiente forma:

# for variable in sequence: 
 #  Code to repeat
 
for neuron in range (1, 6):
    print("neuron")

# Range()
# Range(5) → Produce 0 1 2 3 4 
# Y Range(6) → Produce 1 2 3 4 5
# La regla es, el primer número está incluido y el último excluído. 
# Y con f-string presentamos de mejor manera el output

# Exercise 1 - Neuron counter
# We will use a for loop to iterate through a range of neurons,
# The loop should print the number of each neuron from 1 to 10.

for neuron in range(1, 11):
    print(f"The current neuron is: {neuron}")
    
# Exercise 2 - Counting neural samples 
# Now we are going to use the loop for represent data samples. 
# Suppose we have 20 neurons data samples

sample_count = 20

for sample in range(1, sample_count + 1):
    print(f"Analyzing sample {sample}")
    
# Exercise 3 - Neural firing rates 
# Now we are going to add a little bit of logic on a loop 
# Suppose we need to analyze 10 measurements of firing rate

firing_rate = 2

for iteration_number in range(1, 11):
    print(f"Measurement {iteration_number}: {firing_rate * iteration_number} Hz")
    
# Exercise 4 - Firing rate classification
# The goal here is classificate the measurement: 
#Measurement 1: 5 Hz → Low firing rate
#Measurement 2: 10 Hz → Moderate firing rate ...
#Measurement 10: 50 Hz → High firing rate

firing_rate = 4

for measurement in range(1, 10 + 1): # 10 + 1 → To include 10 in the range.
    if firing_rate * measurement < 10:
        print(f'Measurement: {firing_rate * measurement} Hz → Low firing rate')
    elif 10 <= firing_rate * measurement <= 30:
        print(f'Measurement: {firing_rate * measurement} Hz → Moderate firing rate')
    else:
        print(f'Measurement: {firing_rate * measurement} Hz → High firing rate')
        
# Exercise 5: Healthy neurons 
# We have 10 neurons and we want to analyze their firing rate
# Only healthy neurons should be analyzed

firing_rate = 2

for measurement in range(1, 10 + 1): # 10 + 1 → To include 10 in the range.
    firing_rate = measurement * firing_rate
    is_healthy = 10 <= firing_rate 
    if not is_healthy:
        print(f'Neuron {measurement}: {firing_rate} Hz → Not suitable for analysis')
    elif firing_rate <= 30:
        print(f'Neuron {measurement}: {firing_rate} Hz → Moderate')
    else:
        print(f'Neuron {measurement}: {firing_rate} Hz → High')

# Variables & Conditionals — Integration Exercises

# Exercise 1 - Neuron age screening 
# A research team wants to analyze neurons from adult subjects.
# Classify the subject: Under 18 → Underage ; 18 - 40 → Suitable age ; Above 40 → Outside the target range
# Use if / elif / else and comparison operators

age = 40

if age < 18:
    print(f'The subject is underage')
elif 18 <= age <= 40:
    print(f'Suitable age')
else:
    print(f'Outside the target range')

# Exercise 2 - Membrane potential
# A neuron has a membrane potential and a resting potential 

membrane_potential = -55
resting_potential = -55

if membrane_potential < resting_potential:
    print(f'Below resting potential')
elif membrane_potential == resting_potential:
    print(f'At resting potential')
else:
    print(f'Above resting potential')
    
# Exercise 3 - Action potential threshold
# Determine whether the neuron has reached the action potential threshold
# Use a Boolean condition 

membrane_potential = -70
threshold = -70

#Option 1 → Whitout a boolean condition
if membrane_potential >= threshold:
    print(f'Action potential threshold reached')
else:
    print(f'Threshold not reached')

#Option 2 → With a boolean condition
threshold_reached = membrane_potential >= threshold
if threshold_reached:
    print(f'Action potential threshold reached')
else:
    print(f'Threshold not reached')

# Exercise 4 - Firing rate classification
# Classify the neural activity 
# Below 10 Hz → Low ; 10-30 Hz → Medium ; Above 30 Hz → High
# Print the firing rate together with the classification
# For example: Firing rate: 25 Hz → Moderate

firing_rate = 5

if firing_rate < 10:
    print(f'Firing rate is: {firing_rate} Hz → Low')
elif 10 <= firing_rate <= 30:
    print(f'Firing rate is: {firing_rate} Hz → Moderate')
else:
    print(f'Firing rate is: {firing_rate} Hz → High')
    
# Exercise 5 - Neuron type
# Evaluate what kind of neuron is: 
# The possible values are: sensory, excitatory, inhibitory
# If another value is provided → Unknown neuron type

neuron_type = "inhibsssitory"

if neuron_type == "sensory":
    print('A sensory neuron converts internal or external stimuli into electrical impulses and transmits them to the central nervous system.')
elif neuron_type == "excitatory":
    print('An excitatory neuron releases neurotransmitters that depolarize the postsynaptic membrane, increasing the probability of generating an action potential.')
elif neuron_type == "inhibitory":
    print('An inhibitory neuron releases neurotransmitters that hyperpolarize the postsynaptic membrane, reducing the probability that the postsynaptic neuron will generate an action potential.')
else: 
    print('Unknown neuron type')    
    
# Exercise 6 - Neuron suitability
# A neuron is suitable for an experiment only if:
    # 1 - It is healthy
    # 2 - A recording is available
    # 3 - Its age is beetween 18 and 40
    # 4 - Its firing rate is between 10 and 50 Hz
    
age = 25
firing_rate = 5
is_healthy = True
is_recording = True

if is_healthy and is_recording and 18 <= age <= 40 and 10 <= firing_rate <= 50:
    print('The neuron is suitable for the experiment')
else:
    print('Neuron is not suitable for the experiment')
    
# Exercise 7 - Recording control
# A neural recording can only be analyzed if a recording is currently available
# If there is no recording → "No neural recording available"
# Otherwise classify the firing rate: 
    # Below 10 Hz     → Low neural activity
    # 10–40 Hz        → Moderate neural activity
    # Above 40 Hz     → High neural activity
# Hint: This is a good place to use not.

firing_rate = 5
is_recording = True

if not is_recording:
    print('No neural recording available')
elif 10 > firing_rate:
    print(f'The firing rate is: {firing_rate} Hz → Low neural activity')
elif 10 <= firing_rate <= 40:
    print(f'The firing rate is: {firing_rate} Hz → Moderate neural activity')
else:
    print(f'The firing rate is: {firing_rate} Hz → High neural activity')
    
# Exercise 8 - Neuron activation 
# A neuron is considered activated only when both conditions are satisfied:
    # 1 - Its membrane potential has reached or exceeded the threshold
    # 2 - The neuron is healthy
# Determine whether the neuron is activated 

membrane_potential = -55
threshold = -55
is_healthy = True

if is_healthy and membrane_potential >= threshold:
    print('The neuron is activated')
else:
    print('The neuron is not activated')

# Exercise 9 - Analyze multiple neurons
# Now we bring the 'for' loop back
# Suppose you have 10 neurons
# Each neuron has a firing rate that increases by 5 Hz
# For each neuron, classify its firing rate: 
    # Below 10 Hz     → Low 
    # 10–30 Hz        → Moderate
    # Above 30 Hz     → High

for neuron in range(1, 10 + 1):
    firing_rate = 5 * neuron
    if firing_rate < 10:
        print(f'Neuron {neuron} → {firing_rate} Hz → Low')
    elif 10 <= firing_rate <= 30:
        print(f'Neuron {neuron} → {firing_rate} Hz → Moderate')
    else:
        print(f'Neuron {neuron} → {firing_rate} Hz → High')

# Exercise 10 - Neural Data Screening
# You have 10 neurons
# For each neuron: 
    # Its firing rate increases by 5 Hz
    # The neuron is considered suitable if its firing rate is 10 Hz or higher
    # Only suitable neurons should be classified
    # For suitable neurons → 10 - 30 Hz → Moderate activity ; Above 30 Hz → High activity
    # For unsuitable neurons → Neuron X: Not suitable for analysis
    
for neuron in range(1, 10 + 1):
    firing_rate = 5 * neuron
    if firing_rate < 10:
        print(f'Neuron {neuron}: {firing_rate} Hz → Not suitable for analysis')
    elif 10 <= firing_rate <= 30:
        print(f'Neuron {neuron}: {firing_rate} Hz → Moderate activity')
    else:
        print(f'Neuron {neuron}: {firing_rate} Hz → High activity')
        
# Integration: Round 2

# Exercise 1 - Neuron viability
print("Exercise 1 - Neuron viability")
# A laboratory has a neuron with the following characteristics: 
    # Membrane potential: -60 mV
    # Resting potential: -70 mV
    # The neuron is healthy. 
# Determine whether the neuron is viable for recording

# A neurons is viable if:
    # It is healthy
    # Its membrane potential is at or above its resting potential
        # Print either "Neuron is viable for recording" - "Neuron is not viable for recording"

membrane_potential = -70 
resting_potential = -70
is_healthy = True

if is_healthy and membrane_potential >= resting_potential:
    print('The neuron is viable for recording')
else:
    print('The neuron is not viable for recording')

# Exercise 2 — Firing threshold 
print("Exercise 2 — Firing threshold")
# A neuron has: -52 mV of membrane potential & threshold of -55 mV.
# Determine wheter the neuron has reached the threshold
# Then print the membrane potential and result.

membrane_potential = -52 
threshold = -55 
result = membrane_potential >= threshold

if result:
    print(f'The membrane potential is {membrane_potential} mV and has reached the threshold')
else:
    print(f'The membrane potential has not reached the threshold')

# Exercise 3 - Experimental subjects
print("Exercise 3 - Experimental subjects")

# A researcher wants neurons from subjects between 20 and 35 years old
# The neuron also needs to be healthy.
# Create the necessary variables and determine whether the subject can participate in the experiment

age_of_subject = 35
is_healthy = True

if is_healthy and 20 <= age_of_subject <= 35:
    print(f'The subject age is: {age_of_subject} and can participate in the experiment')
else:
    print("The subject can't participate in the experiment")
    
# Exercise 4 - Neural activity warning
print("Exercise 4 - Neural activity warning")
# A recording system measures a firing rate
# Classify it: 
    # < 10 Hz       → Low activity
    # 10 - 40 Hz    → Normal activity
    # > 40 Hz       → High activity
# If the firing rate is above 60 Hz, print "Warning: unusually high activity" instead

firing_rate = 100

if 10 > firing_rate:
    print(f'The firing rate is: {firing_rate} Hz → Low activity')
elif 10 <= firing_rate <= 40:
    print(f'The firing rate is: {firing_rate} Hz → Normal activity')
else:
    if firing_rate > 60:
        print(f'The firing rate is: {firing_rate} Hz → Warning: Unusually high activity')
    else:
        print(f'The firing rate is: {firing_rate} → High activity')

# Exercise 5 - Recording availability
print("Exercise 5 - Recording availability")

# The neural data can only be analyzed if:
    # a recording is available
    # AND the neuron is healthy
# If there is no recording: "No recording available"
# If there is a recording but the neuron isn't healthy: "Neuron is not healthy"
# Otherwise: Ready for analysis

is_recording = True
is_healthy = False

if not is_recording:
    print('No recording available')
elif not is_healthy:
    print('Neuron is not healthy')
else:
    print('Ready for analysis')

# Exercise 6 - Neuron counter
print("Exercise 6 - Neuron counter")
# A researcher wants to inspect 15 neurons

for neuron in range(1, 15 + 1):
    print(f'Analyzing neuron {neuron}')
    
# Exercise 7 - Increasing firing rate
print("Exercise 7 - Increasing firing rate")
# A hypothetical experiment starts with a firing rate of 5 Hz.
# For each of 10 neurons, the firing rate increases by 5 Hz. 
# Then classify each neuron: 
    # < 10 Hz    → Low
    # 10 - 30 Hz → Moderate
    # > 30 Hz    → High

for neuron in range(1, 10 + 1):
    firing_rate = 5 * neuron
    if firing_rate < 10:
        print(f'Neuron {neuron}: {firing_rate} Hz → Low')
    elif 10 <= firing_rate <= 30:
        print(f'Neuron {neuron}: {firing_rate} Hz → Moderate')
    else:
        print(f'Neuron {neuron}: {firing_rate} Hz → High')

# Exercise 8 - Healthy firing rate 
print("Exercise 8 - Healthy firing rate")

# For each for 10 neurons: 
# A neuron is considered healthy for the experiment if its firing rate is between 10 and 40 Hz, inclusive. 
# If it isn't → Neuron x → Not suitable 
# If it is → Neuron x → Suitable
# Don't classify its activity yet. Focus only on the boolean condition.


for neuron in range(1, 11):
    firing_rate = 5 * neuron
    is_healthy = 10 <= firing_rate <= 40
    if not is_healthy:
        print(f'Neuron {neuron} → Is not suitable')
    else:
        print(f'Neuron {neuron} → Suitable ')

# Exercise 9 - Suitable neuron + activity
print("Exercise 9 - Suitable neuron + activity")
# Now combine exercises 7 and 8
# For each neuron: 
    # 1 - Calculate its firing rate
    # 2 - Determinate whether it is suitable
    # 3 - If it isn't suitable, report that
    # 4 - If it's suitable, classify its activity: 10 - 20 Hz → Low ; 21 - 40 Hz Moderate

for neurons in range(1, 10 + 1):
    firing_rate = 5 * neurons
    is_healthy = 10 <= firing_rate <= 40
    
    if not is_healthy:
        print(f"Neuron: {neurons} → Isn't suitable")
    elif 10 <= firing_rate <= 20:
        print(f'Neuron: {neurons} → Low')
    else:
        print(f'Neuron: {neurons} → Moderate')
        
# Exercise 10 - Mini neural screening system
print("Exercise 10 - Mini neural screening system")
# You've 10 neurons
# For each neuron: 
    # Firing rate starts at 5 Hz and increase by 5 Hz
    # A neuron is suitable if its firing rate is between 10 and 40 Hz, inclusive.
    # Only suitable neurons should be analyzed
    # Suitable neurons with: 
        # 10 - 20 Hz → Low activity
        # 21 - 40 Hz → Moderate activity
    # Anything outside the healthy range should be reported as: "Neuron X → Not suitable for analysis"

for neurons in range(1, 10 + 1):
    firing_rate = 5 * neurons
    is_healthy = 10 <= firing_rate <= 40

    if not is_healthy:
        print(f'Neuron: {neurons} → {firing_rate} Hz → Not suitable for analysis')
    elif 10 <= firing_rate <= 20:
        print(f'Neuron: {neurons} → {firing_rate} Hz → Low activity')
    else:
        print(f'Neuron: {neurons} → {firing_rate} Hz → Moderate activity')
    