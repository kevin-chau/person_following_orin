def calculate_averages_from_log_file(filepath):
    import re

    
    patterns = {
        "Monocular person following node callback execution time": r"Monocular person following node callback execution time: (\d+) ms",
        "UKF Tracker prediction and correction": r"UKF Tracker prediction and correction took: ([\d.]+)s",
        "CCF Feature extraction": r"CCF Feature extraction took: ([\d.]+)s",
        "Monocular people tracking node callback execution time": r"Monocular people tracking node callback execution time: (\d+) ms"
    }

    
    results = {key: [] for key in patterns}

    
    with open(filepath, 'r') as file:
        for line in file:
            for key, pattern in patterns.items():
                match = re.search(pattern, line)
                if match:
                    value = float(match.group(1))
                    results[key].append(value)

    
    averages = {key: sum(values) / len(values) if values else None for key, values in results.items()}
    return averages


filepath = 'testing3.txt'  
average_times = calculate_averages_from_log_file(filepath)
print(average_times)
