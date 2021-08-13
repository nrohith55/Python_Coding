
nums=[10,12,13,14,15]

for num in nums:

    if num%5==0:  # It will check for the first num and breaks the loop
        print(num)
    break

else:
    print("not found")