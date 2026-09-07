# Exercise 1 — Basic Lambda
# Create a lambda function that receives a number and returns its square.
# Test it with several different numbers.
# Then create another lambda function that receives a number and returns its cube.

square = lambda number: number **2
print(square(44))
cube = lambda num: num **3
print(cube(44))

# Exercise 2 — Even or Odd
# Create a lambda function that receives a number.
# It should return:
# - "even" if the number is even
# - "odd" if the number is odd
# Test it with several positive and negative integers.
even_or_odd = lambda num: "Even" if num % 2 == 0 else "Odd"
print(even_or_odd(44))

# BUILD-IN FUNCTION MORE USED ON LAMBDA FUNCTIONS
    # sort() function → with a lambda function as parameter
# Exercise 3 — Custom Sorting
# Use sorted() to order the neurons by firing_rate.
# The original list should remain unchanged.
# Use a lambda function to tell sorted()
# which value should be used for ordering.
# Print the ordered result.
neurons = [
    {"type": "excitatory", "firing_rate": 45},
    {"type": "inhibitory", "firing_rate": 80},
    {"type": "sensory", "firing_rate": 30},
    {"type": "excitatory", "firing_rate": 65}
]
neurons_sorted_by_firing_rate = sorted(neurons, key=lambda neuron: neuron["firing_rate"])
neurons_sorted_by_type = sorted(neurons, key=lambda neuron: neuron["type"])
print(f'By firing rate: {neurons_sorted_by_firing_rate}\nBy type: {neurons_sorted_by_type}')

    
    # filter() function → with a lambda for filter by condition
# Exercise 4 — Neural Filtering
# Create a list containing several neuron dictionaries.
# Each neuron should have:
# - type
# - firing_rate
# Use filter() and a lambda function to obtain only the neurons with a firing_rate greater than 50.
# Convert the result into a list.
# Test the result with several neurons.

neurons = [
    {"type": "excitatory", "firing_rate": 45},
    {"type": "inhibitory", "firing_rate": 80},
    {"type": "sensory", "firing_rate": 30},
    {"type": "excitatory", "firing_rate": 65}
]
neurons_filtered_by_firing_rate = list(filter(lambda neuron: neuron["firing_rate"] > 50, neurons))
print(f'Filtered by firing rate > 50: {neurons_filtered_by_firing_rate}')

    
    # map() function → with a lambda for filter by condition
# Exercise 5 — Extract Firing Rates
# Use map() and a lambda function to extract the firing_rate from every neuron.
# Convert the result into a list.
# Store the result in a new variable.
# The original list should remain unchanged.

mapped_firing_rates = list(map(lambda neuron: neuron['firing_rate'] * 2, neurons))
print(f'Mapeated: {mapped_firing_rates}') 
print(f'{neurons}') # Corroboro que la lista esté igual
print(f'{type(map)}') # Corroboro que la lista esté igual

# Exercise 6 — Neural Data Pipeline
# Create a list of neurons with:
# - type
# - firing_rate
# Build a small processing pipeline:
# 1. Keep only neurons with a firing_rate greater than 40.
# 2. Extract their firing_rate values.
# 3. Order the resulting values from highest to lowest.
# Use filter(), map(), sorted(), and lambda functions.
# Store the final result in a variable and print it.
# Do not modify the original list.

neurons_procesed = list(sorted(map(lambda neuron:neuron['firing_rate'],filter(lambda neuron: neuron['firing_rate'] > 40, neurons)), reverse=True))

print(neurons_procesed)