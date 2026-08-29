# Exercise 1 — Neuron type

neuron_type = "sensory" 

if neuron_type == "sensory":
    print("This neuron is responsible for transmitting sensory information.")
else:
    print("This is another type of neuron.")
    
# Exercise 2 - Membrane potential 
# A neuron's resting membrane potential is approximately -70mV.
# Then determine whether the neuron's membrane potential is at or above its typical resting potential.

membrane_potential = -70
resting_potential = -70

if membrane_potential < resting_potential:
    print("The membrane potential is below resting potential")
else:
    print("The membrane potential is at or above resting potential")
    
# Exercise 3 - Action potential threshold
# A neuron typically reaches the action potential threshold at approximately -55mV.
# Determine whether the neuron has reached the threshold.

membrane_potential = -50
threshold = -55

if membrane_potential >= threshold:
    print("Action potential threshold reached.")
else: 
    print("Threshold not reached")
    
# Exercise 4 - Firing rate
# A neuron's firing rate describes how frequently it generates action potentials, measured in Hertz (Hz).
# Classify the neuron's firing rate:
    # Less than 10 Hz   → Low firing rate
    # 10 - 30 Hz        → Moderate firing rate
    # More than 30 Hz   → High firing rate

firing_rate = 10

if firing_rate < 10:
    print("Low firing rate")
elif 10 <= firing_rate <= 30:
    print("Moderate firing rate")
else:
    print("High firing rate")

# Exercise 5 - Synaptic strength 
# Classify the synaptic connection: 
    #Below 0.3      → Weak synaptic connection
    #0.3 - 0.7      → Moderate synaptic connection
    #Above 0.7      → Strong synaptic connection

synaptic_strength = 0.71

if synaptic_strength < 0.3:
    print("Weak synaptic connection")
elif 0.3 <= synaptic_strength <= 0.7:
    print("Moderate synaptic connection")
else:
    print("Strong synaptic connection")

#Exercise 6 — Excitatory or inhibitory neuron
#The program should determine the effect of the neuron:
    #"excitatory"  → This neuron increases the likelihood of firing.
    #"inhibitory"  → This neuron decreases the likelihood of firing.
    #anything else → Unknown neuron type.
    
neuron_type = "inhibitory"

if neuron_type == "inhibitory":
    print("This neuron decreases the likelihood of firing")
elif neuron_type == "excitatory":
    print("This neuron increases the likelihood of firing")
else:
    print("Unknown neuron type")
    
#Exercise 7 — Neuron activation
#Now we are going to combine two types of information
#The neuron is considered activated only if: 
    # 1 - Its membrane potential has reached or exceeded the threshold
    # 2 - The neuron is healthy 

membrane_potential = -52
threshold = -55
is_healthy = True

if membrane_potential >= threshold and is_healthy:
    print("Neuron is activated")
else:
    print("Neuron is not activated")
    
# Exercise 8 — Experimental neuron
# A neuron is considered suitable for the experiment only if:
    # 1 - It is healthy.
    # 2 - Its age is between 18 and 40. 
    # 3 - Its firing rate is between 10 and 50 Hz.

age = 18
firing_rate = 35
is_healthy = True

if 18 <= age <= 40 and 10 <= firing_rate <= 50 and is_healthy:
    print("Neuron is suitable for the experiment")
else: 
    print("Neuron is not suitable for the experiment")

# Exercise 9 - Neural activity
# Classify the neural activity, but only if a recording is currently being made.

firing_rate = 11
is_recording = True

if is_recording and 10 > firing_rate:
    print("Low neural activity")
elif is_recording and 10 <= firing_rate <= 40:
    print("Moderate neural activity")
elif is_recording and 40 < firing_rate:
    print("High neural activity")
else:
    print("No neural recording available")
    
# Exercise 9.1 - Neural activity with control flow
# Classify the neural activity, but only if a recording is currently being made.

firing_rate = 41
is_recording = False

if not is_recording:
    print("No neural recording availaible")
elif firing_rate < 10:
    print("Low neural activity")
elif 10 <= firing_rate <= 40:
    print ("Moderate neural activity")
else:
    print("High neural activity")
    
#Exercise 10 - Mini Neural Data Assessment

#Suitability for analysis 
#PART A - The neuron is suitable for analysis only if all five conditions are satisfied:
    # 1 - The neuron is healthy.
    # 2 - A recording is availaible
    # 3 - Age is between 18 and 40
    # 4 - Membrane potential has reached or exceeded the threshold
    # 5 - Firing rate is between 10 and 50 hz

#PART B - Firing activity
    # Only if the neuron is suitable, classify its firing activity
    # Below 20 Hz → Low firing activity
    # 20–40 Hz    → Moderate firing activity
    # Above 40 Hz → High firing activity

# Variables    
age = 25
membrane_potential = -52
threshold = -55
firing_rate = 32
is_healthy = True
is_recording = True

# Resolution Part A 

if is_healthy and is_recording and 18 <= age <= 40 and membrane_potential >= threshold and 10 <= firing_rate <= 50:
    print("Neuron is suitable for analysis")
    print("Proceeding to check the firing activity.")
    if firing_rate < 20:
        print("Low firing activity") 
    elif 20 <= firing_rate <= 40:
        print("Moderate firing activity")
    else:
        print("High firing activity")
else: 
    print("Neuron is not suitable for analysis")
    