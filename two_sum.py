def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9

print("Example 1:")
print("Input:", nums1, "Target:", target1)
print("Output:", twoSum(nums1, target1))


# Example 2
nums2 = [3, 2, 4]
target2 = 6

print("\nExample 2:")
print("Input:", nums2, "Target:", target2)
print("Output:", twoSum(nums2, target2))


# Example 3
nums3 = [3, 3]
target3 = 6

print("\nExample 3:")
print("Input:", nums3, "Target:", target3)
print("Output:", twoSum(nums3, target3))
