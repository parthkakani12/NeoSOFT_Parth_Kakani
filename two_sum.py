
def twoSum(nums, target):# Function to find the indices of two numbers that add up to the target

    seen = {}# Dictionary to store numbers and their indices

    for i, num in enumerate(nums):# Traverse through the list
        complement = target - num # Calculate the number needed to reach the target

        if complement in seen:# Check if the required number has already been seen
            return [seen[complement], i] # Return the indices of the two numbers

        seen[num] = i# Store the current number and its index


nums1 = [2, 7, 11, 15]
target1 = 9

print("Example 1:")
print("Input:", nums1, "Target:", target1)
print("Output:", twoSum(nums1, target1))



nums2 = [3, 2, 4]
target2 = 6

print("\nExample 2:")
print("Input:", nums2, "Target:", target2)
print("Output:", twoSum(nums2, target2))



nums3 = [3, 3]
target3 = 6

print("\nExample 3:")
print("Input:", nums3, "Target:", target3)
print("Output:", twoSum(nums3, target3))
