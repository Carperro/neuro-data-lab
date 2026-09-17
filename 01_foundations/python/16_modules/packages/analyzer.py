import statistics as stats
values = [10, 20, 30]
def analyze_population(values):
    
    statistics = stats.calculate_statistics(values)
    results = {
        "average": statistics["average"],
        "highest_value": statistics["highest_value"],
        "lowest_value": statistics["lowest_value"],
        "total": statistics["total"],
    }
    return results

result = analyze_population(values)
print(result)