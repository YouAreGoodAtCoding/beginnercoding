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


if __name__ == "__main__":
    nums = [2, 4, 3, 5, 7]
    target = 7
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # edge cases
    # 1. Empty list
    nums = []
    target = 7
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # 2. No valid pairs
    nums = [1, 4, 5, 7]
    target = 7
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # 3. Negative numbers
    nums = [-1, -2, 3, 5]
    target = 2
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # 4. Duplicates numbers
    # a. same pair, is ok, as long as numbers are present twice.
    nums = [1, 1, 5, 5]
    target = 6
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # b. same number twice in same pair (if actually present twice), is ok
    nums = [3, 5, 3, 5]
    target = 6
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))

    # c. same number twice in different pairs (if not actually present twice) is not ok.
    nums = [2, 4, 3, 5, 7, 4, 1]
    target = 7
    target_pairs = findTargetSumPairs(nums, target)
    print(", ".join([str(tuple) for tuple in target_pairs]))
