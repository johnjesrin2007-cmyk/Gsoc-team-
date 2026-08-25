word = "mississippi"
frequency={}

for l in word:
    if l not in frequency:
        frequency[l]=1
    else:
        frequency[l]+=1

print(frequency)