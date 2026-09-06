# Find divisors for N
def find_divisors(num):
    d = 1
    divisors = set()
    while True:
        d2 = num // d
        if d > d2:
            break
        if num % d == 0:
            divisors.add(d)
            divisors.add(d2)
        d += 1
    return divisors
result = find_divisors(17)
print(result)
# Exercise 2 — Perfect Number Analysis
# Create a function called is_perfect_number().
# The function should receive a positive integer.
# Determine whether the number is equal to the sum of all its positive divisors excluding itself.
# Return True if it is a perfect number.
# Return False otherwise.
# Test the function with several different numbers.
# Examples:
# 6 is a perfect number because its proper divisors are:
# 1, 2, 3
# 1 + 2 + 3 = 6
# 8 is not a perfect number.

def is_perfect_number(num):
    divisors = find_divisors(num)
    divisors.remove(num)
    return num == sum(divisors)

result = is_perfect_number(41)
print(result)

# Exercise 3 — Divisor Sum Analysis
# Create a function called analyze_divisors().
# The function should receive a positive integer.
# Determine:
# - all positive divisors excluding the number itself
# - the sum of those divisors
# - whether the sum is smaller than, equal to, or greater than the original number
# Return all the results together in a structured form.
# Test the function with several different numbers.

def analyze_divisors(num):
    divisors = find_divisors(num)
    divisors.remove(num)
    total_divisors = sum(divisors)
    if total_divisors < num:
        compare = 'smaller than'
    elif total_divisors == num:
        compare = 'equal to'
    else:
        compare = 'greater than'
    to_output = {
    'sum_divisor': total_divisors,
    'divisors': divisors,
    'compare': compare
    }
    return to_output

# Exercise 4 — Abundant and Deficient Numbers
# Create a function called classify_number().
# The function should receive a positive integer.
# Calculate the sum of its proper divisors.
# Determine whether the number is:
# - deficient
# - perfect
# - abundant
# Return the classification.
# Test the function with several different numbers.
# Examples:
# 8 is deficient.
# 6 is perfect.
# 12 is abundant.

def classify_number(num):
    divisors = find_divisors(num)
    divisors.remove(num)
    sum_divisors = sum(divisors)
    if sum_divisors < num:
        return 'deficient'
    elif sum_divisors == num:
        return 'perfect'
    else:
        return 'abundant'

# Exercise 5 — Number Classification Report
# Create a function called generate_number_report().
# The function should receive a list of positive integers.
# For every number, determine whether it is:
# - deficient
# - perfect
# - abundant
# Return a structured result containing:
# - each number
# - its classification
# Test the function with at least ten numbers.
# Include deficient, perfect, and abundant numbers.
numbers = [1, 2, 6, 8, 12, 20, 28, 30, 36, 40, 48, 50, 54, 60, 100]

def generate_number_report(numbers):
    to_output = []
    for num in numbers:
        number_classification = classify_number(num)
        number_classified = (num,number_classification)
        to_output.append(number_classified)
    return to_output

results = generate_number_report(numbers)
print(results)

