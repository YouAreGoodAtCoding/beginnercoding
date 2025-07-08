

# warm up
# c is any character, caps or small, alphabet or numbers or any special character
def isVowel(c):
    c = str.lower(c)
    if c in "aeiou":
        return True
    else:
        return False

# string contains any character, caps or small, alphabet or numbers or any special character


def countVowels(str_input):
    cnt = 0
    for c in str_input:
        if (isVowel(c)):
            cnt += 1

    return cnt


if __name__ == "__main__":

    # input = 'umbrella'
    # input = 'UmbreLla'
    # input = ""
    # input = "e"
    # input = "f"
    # input = "&*(@#&@())"
    # input = "125Um!breLla%6*"
    input = "Beautiful day"

    # test warm up
    # for c in input:
    #     if (isVowel(c)):
    #         print(f"{c} is a vowel")

    cnt = countVowels(input)
    print(f"{input} has {cnt} vowels in it")
