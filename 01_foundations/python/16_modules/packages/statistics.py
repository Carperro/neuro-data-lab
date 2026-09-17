numbers = [10,6,7,11,-23,54,34,37,0,-15,-27,100,6.999,-12]

def calculate_statistics(numbers):
    total = 0
    for number in numbers:
        total += number
    numbers.sort()
    highest_value = numbers[-1]    
    lowest_value = numbers[0]    
    average = total / len(numbers)
    results = {
        "average": average,
        "highest_value": highest_value,
        "lowest_value": lowest_value,
        "total": total
        }
    return results