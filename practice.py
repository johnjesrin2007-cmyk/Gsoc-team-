numbers = [5, 8, 12, 5, 8, 20, 12, 5, 8, 20, 12, 20]
frequency = {}
highest_frequency = None
most_frequent = None

for i in range(len(numbers)):
        if numbers[i] not in frequency:
            frequency[numbers[i]] = 1
        else:
            frequency[numbers[i]] += 1

for key, values in frequency.items():
    if highest_frequency is None or values > highest_frequency:
        highest_frequency = values
        most_frequent = key

print("Element:", most_frequent)
print("Frequency:", highest_frequency)