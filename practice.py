numbers = [4, 2, 7, 1, 6, 3]
prefix=[]
total=0

for num in numbers:
    total+=num
    prefix.append(total)

print(prefix)

summ=prefix[5]-prefix[1]

print(summ)