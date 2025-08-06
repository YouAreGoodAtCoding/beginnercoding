""" Given an input String str that consists only of upper/lowercase english characters and spaces

Return an Array/List of Strings that holds every space seperated word from str.

input = "The brown fox jumps over the lazy dog"
Returns ["The","brown","fox","jumps","over","the","lazy","dog"]

Your language likely has a built in split() method so also try without it ;3
 """


def splitSentence(input: str):
    temp_char_arr = []
    result_str_arr = []
    for c in input:
        if (c != ' '):
            temp_char_arr.append(c)
        else:
            result_str_arr.append(''.join(temp_char_arr))
            temp_char_arr = []
    return result_str_arr


def testSplitSentence():
    input = "The brown fox jumps over the lazy dog"
    output = splitSentence(input)
    print(f"{input} split is {output}")


# Given an input integer array nums split it into non-decreasing sub arrays.
# nums = [3, 4, 5, 2, 2, 5, 3]
# returns [[3, 4, 5], [2, 2, 5], [3]]
def splitArrays(input):
    output = []
    temp = []
    prev = None
    for curr in input:
        if (prev is not None and (prev > curr)):
            output.append(temp)
            temp = [curr]
        else:
            temp.append(curr)
        prev = curr
    output.append(temp)
    return output


def testSplitArrays():
    nums = [3, 4, 5, 2, 2, 5, 3]
    output = splitArrays(nums)
    print(f"{nums} split is {output}")


# add two big integers represented as arrays and return the result as another array.
def addBigIntegers(num1, num2):
    i1 = len(num1)-1
    i2 = len(num2)-1
    output = []
    carry = 0

    while (i1 >= 0 or i2 >= 0):
        sum = carry
        if (i1 >= 0):
            sum += num1[i1]

        if (i2 >= 0):
            sum += num2[i2]

        # carry over
        if sum > 9:
            carry = int(sum / 10)
            sum = sum % 10

        output.insert(0, sum)
        i1 -= 1
        i2 -= 1

    if carry != 0:
        output.insert(0, carry)

    return output


def testAddBigIntegers():
    num1 = [9]
    num2 = [1]
    output = addBigIntegers(num1, num2)
    print(f"Sum of {num1} and {num2} is {output}")

    num1 = [9, 8, 1, 0, 1]
    num2 = [2, 3]
    output = addBigIntegers(num1, num2)
    print(f"Sum of {num1} and {num2} is {output}")

    num1 = [9, 9, 1, 0, 1]
    num2 = [9, 9, 2, 3]
    output = addBigIntegers(num1, num2)
    print(f"Sum of {num1} and {num2} is {output}")


# Given a binary integer digits representing a binary number where digits[i] is the ith digit of the binary number
# return the decimal representation of the number
def binaryToDecimal(arr):
    # digits = [1,0] returns 2
    sum = 0
    i = len(arr)-1
    while (i >= 0):
        sum += arr[i] * 2 ** ((len(arr)-1)-i)
        i -= 1
    return sum


def testBinaryToDecimal():
    digits = [1, 0, 1]
    output = binaryToDecimal(digits)
    print(f"Binary {digits} is {output}")


if __name__ == '__main__':
    testBinaryToDecimal()
