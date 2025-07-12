import time


# warmup part 1
# this simple and easy to understand. but not so efficient.
# both time and space O(n^2) (allocate a new string, copy each character at every step and add the new character)
# Each time you do rev = c + rev, Python creates a new string by copying both c and rev, because strings are immutable.
# So for an input of length n, this results in creating:
# A new string of length 1, then 2, then 3, ..., up to n.
# This is the sum: 1 + 2 + 3 + ... + n = O(n²) characters copied over the entire loop.
def reverseNotEfficient(input: str):
    rev = ""
    for c in input:
        rev = c + rev
    return rev


# Warm up reverse part 2
# time O(n), space O(n)
# This is the most efficient and Pythonic way to reverse a string, if
# you are not allowed to use slicing (s[::-1]) which has same complexities.
def reverseEfficient(input: str):
    chars = []
    for i in range(len(input) - 1, -1, -1):
        chars.append(input[i])

    reversed_s = ''.join(chars)
    return reversed_s


# yet another efficient way. same time O(n) and space O(n)
# in some other programming languages where strings are mutable,
# we can save extra memory, by doing what we do below on the same input string inplace.
# by using two pointers, one from the end and another from start and swap the elements until we reach middle
def reverseEfficient2(input: str):
    chars = list(input)
    i = 0
    j = len(chars)-1
    while (i < j):
        t = chars[i]
        chars[i] = chars[j]
        chars[j] = t
        i += 1
        j -= 1

    reversed_s = ''.join(chars)
    return reversed_s


def isAlpha(c: str):
    return ('a' <= c <= 'z' or 'A' <= c <= 'Z')


# Ignore upper/lowercase when comparing.
# Ignoring spaces and punctuation.
def normalize(input: str):
    norm_chars = []
    for c in input:
        if isAlpha(c):
            norm_chars.append(c.lower())
    return ''.join(norm_chars)


###
# main challenge part 1
# It's not so efficient, but simple and easy to understand.
# you can literally take the definition of palindrome and code it up.
# definition of palindrome: the string should read the same even if it is reversed.
# time: O(n^2), space O(n^2)
###
def isPalindromeInEfficient(input: str):
    input = normalize(input)
    rev = ""
    for c in input:
        rev = c + rev
    return rev == input


###
# main challenge part 2
###
def isPalindromeEfficient(input: str):
    input = normalize(input)
    # print(f"normalized input: {input}")
    i = 0
    j = len(input)-1
    while (i < j):
        if not (input[i] == input[j]):
            return False
        i = i+1
        j = j-1
    return True


if __name__ == "__main__":
    # max for my laptop 10^9, before process killed due to memory limitation
    input = "a" * (10**6)
    print(len(input))

    start = time.time()
    reversed = reverseNotEfficient(input)
    end = time.time()
    print(f"Inefficient reverse time taken: {end - start:.6f} seconds")

    start = time.time()
    reversed = reverseEfficient(input)
    end = time.time()
    print(f"Efficient reverse time taken:   {end - start:.6f} seconds")

    start = time.time()
    reversed = reverseEfficient2(input)
    end = time.time()
    print(f"Efficient2 reverse time taken:   {end - start:.6f} seconds")

    start = time.time()
    print(f"Is the large string a palindrome?: {isPalindromeEfficient(input)}")
    end = time.time()
    print(
        f"Efficient palindrome checker time taken:   {end - start:.6f} seconds")

    # not a palindrome
    input = "34AfZ`54SDd?za#"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # odd palindrome
    input = "m a#d&aM"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # even palindrome
    input = "Raccar"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # two char palindrome
    input = "ww"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # two char not palindrome
    input = "rw"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # one char
    input = "r"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # empty
    input = ""
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")

    # bonus
    input = "A man a plan a canal Panama"
    print(f"Is {input} a palindrome?: {isPalindromeEfficient(input)}")
