import array

"""warm up
Given a list of numbers, find all pairs. 
Each pair should include two different elements
e.g. [1,2,3]
returns (1,2) (1,3) (2,3)
Returns:
    None
"""


def findPairs(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            print(f"({nums[i]}, {nums[j]})")


"""main challenge
Given a list of numbers and a target,
write a program that finds all pairs of numbers in the list that add up to the target.

Time complexity: O(n^2)
Space complexity: O(n)
Returns:
    list of pairs as tuples
"""


def findTargetSumPairs(nums, target):
    n = len(nums)

    taken = array.array("i", [0] * n)

    target_pairs = []
    for i in range(0, n):
        for j in range(i+1, n):
            if (taken[i] == 0 and taken[j] == 0 and nums[i] + nums[j] == target):
                target_pairs.append((nums[i], nums[j]))
                taken[i] = 1
                taken[j] = 1
    return target_pairs


# warm up
# counts how many times each number appears in a list.
def countFrequency(nums):
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    return freq_map


def testCountFrequency():
    nums = [2, 4, 2, 3, 4, 4]
    freq_map = countFrequency(nums)

    print(freq_map)


# main challenge
# time complexity O(n)
# space complexity O(n)
def findTargetSumPairsUsingMaps(nums, target):
    seen_freq_map = {}
    target_pairs = []
    for num in nums:
        if num in seen_freq_map:
            seen_freq_map[num] += 1
        else:
            seen_freq_map[num] = 1

        complement = target - num
        if complement in seen_freq_map and seen_freq_map[complement] > 0:
            target_pairs.append((num, complement))
            seen_freq_map[complement] -= 1
            seen_freq_map[num] -= 1
    return target_pairs


def testTargetSumPairs(funcTargetSumPairs):
    nums = [2, 4, 3, 0, 5, 7]
    target = 7
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # edge cases
    # 1. Empty list
    nums = []
    target = 7
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # 2. No valid pairs
    nums = [1, 4, 5, 7]
    target = 7
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # 3. Negative numbers
    nums = [-1, -2, 3, 5]
    target = 2
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # 4. Duplicates numbers
    # a. same pair, is ok, as long as numbers are present twice.
    nums = [1, 1, 5, 5]
    target = 6
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # b. same number twice in same pair (if actually present twice), is ok
    nums = [3, 5, 3, 5]
    target = 6
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # c. same number twice in different pairs (if not actually present twice) is not ok.
    nums = [2, 4, 3, 5, 7, 4, 1]
    target = 7
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # d. same number twice in different pairs (if actually present twice) is ok.
    nums = [2, 4, 3, 5, 7, 4, 1, 3]
    target = 7
    target_pairs = funcTargetSumPairs(nums, target)
    print(f"Test {funcTargetSumPairs}: input: {nums}, target: {target}")
    print(", ".join([str(tuple) for tuple in target_pairs]))


if __name__ == "__main__":
    testTargetSumPairs(findTargetSumPairs)
    testTargetSumPairs(findTargetSumPairsUsingMaps)
