numbers = [3, 8, 12, 4, 7]
target = 11
seen=set()
for num in numbers:
    required=target-num

    if required in seen:
        print(required,num)

    seen.add(num)