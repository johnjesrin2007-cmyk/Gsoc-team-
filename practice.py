numbers1 = [1, 2, 3, 4, 5]
numbers2 = [3, 5, 7, 9]

seen = set(numbers1)

for num in numbers2:
    if num in seen:
        print(num)