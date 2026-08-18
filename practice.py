numbers = [2, 5, 1, 8, 2, 9, 3]
k = 3

window_sum = 0

for i in range(k):
    window_sum += numbers[i]

largest = window_sum

for i in range(k, len(numbers)):
    window_sum += numbers[i]
    window_sum -= numbers[i - k]

    if window_sum > largest:
        largest = window_sum

print("Maximum Sum:", largest)