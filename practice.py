numbers = [1, 4, 6, 6, 6, 6, 9, 12, 15]
target = 6

left = 0
right = len(numbers) - 1
first_occurance=-1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
       first_occurance=mid
       right=mid-1
    elif numbers[mid] < target:
       left = mid + 1
    else:
       right = mid - 1



left=0
right=len(numbers)-1
last_occurance=-1

while left<=right:
    mid=(left+right)//2

    if numbers[mid]==target:
        last_occurance=mid
        left=mid+1
    elif numbers[mid]<target:
        left=mid+1
    else:
        right=mid-1

count=last_occurance-first_occurance+1
print(f"How many times {target} appears is: {count}") 


