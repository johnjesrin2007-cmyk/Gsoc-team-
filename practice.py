numbers = [1, 12, -5, -6, 50, 3]
k = 4


window_sum=0

for i in range(k):
    window_sum+=numbers[i]

max_sum=window_sum

for i in range(k,len(numbers)):
    window_sum+=numbers[i]
    window_sum-=numbers[i-k]

   

    if window_sum>max_sum:
        max_sum=window_sum

average=max_sum/k
print(average)