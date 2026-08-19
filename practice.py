numbers = [0, 1, 0, 3, 12]
#numbers=[1,0,0,3,12]
#numbers=[1,0,0,3,12]
#numbers=[1,3,0,0,12]
#numbers=[1,3,12,0,0]

left=0
right=1

while right<len(numbers):
    if numbers[left]==0 and numbers[right]!=0:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left+=1
        right+=1
    elif numbers[left]==numbers[right]==0:
        right+=1

print(numbers)

