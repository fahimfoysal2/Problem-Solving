# Given a list of numbers, return the 2nd largest value.
# If there is only one value, return that value.
# If there are no values, return None.
# Example:
#   Input: [7, 7, 12, 98, 106]
#   Output: 106

#   Input: [3, 3, 3]
#   Output: 3

#   Input: [0, -1, 2, -3, 4, -5]
#   Output: 2

def second_largest(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    return ("Second Largest: " + str(nums[-2]))

print(second_largest([10, 20, 4, 45, 57, 99]))
