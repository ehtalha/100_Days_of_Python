# Find the Largest
nums = [3, 41, 12, 9, 74, 15]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print(f"The largest number is {largest}")

# The largest number is 74