numbers = [2, 4, 5, 7, 9, 11, 15]
target = 16

left = 0
right = 0

while left < right:
    total = numbers[left] + numbers[right]

    if total > target:
        right -= 1
    elif total < target:
        left += 1
    else:
        print(f"Pair: {(numbers[left], numbers[right])}")
        break