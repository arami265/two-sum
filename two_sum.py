# This function is for the LeetCode description of the problem,
# in which exactly one solution is assumed and valid indices
# are to be returned.
def two_sum_indices_leetcode(nums, target):
    hash_table = {}

    for i in range(0, len(nums)):
        target_complement = target - nums[i]

        if target_complement in hash_table:
            return [hash_table[target_complement], i]

        hash_table[nums[i]] = i

    return False


# This function solves for all solutions and returns a list
# of valid pairs of indices.
def two_sum_indices(nums, target):
    indices = []
    hash_table = {}

    for i in range(0, len(nums)):
        target_complement = target - nums[i]

        if target_complement in hash_table:
            indices.append([hash_table[target_complement], i])

        hash_table[nums[i]] = i

    return indices


# This function solves for all solutions and returns a list
# of valid pairs of values.
def two_sum_values(nums, target):
    values = []
    hash_table = {}

    for i in range(0, len(nums)):
        target_complement = target - nums[i]

        if target_complement in hash_table:
            values.append([target_complement, nums[i]])

        hash_table[nums[i]] = i

    return values


nums = [3, 5, 2, -4, 8, 11]
target = 7

print()
print('Array:                        ', nums)
print('Target:                       ', target, '\n')
print('Indices for LeetCode solution:', two_sum_indices_leetcode(nums, target))
print('Indices for general solution: ', two_sum_indices(nums, target))
print('Values for general solution:  ', two_sum_values(nums, target))
