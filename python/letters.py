# warmup
# python does not have separate char type, they are str of length 1
def isAlphaLib(c: str):
    return c.isalpha()

###
# main challenge
# if c is an alphabet it should fall between a and z as ascii code is in order
###


def isAlpha(c: str):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

# warm up


def isNotAlpha(c: str):
    return not ('a' <= c <= 'z' or 'A' <= c <= 'Z')

###
# main challenge
# Input: 'f' → Output: lowercase
# Input: 'Q' → Output: uppercase
# Input: '4' → Output: digit
# Input: '#' → Output: symbol
###


def categorize(c: str):
    if 'a' <= c <= 'z':
        return "lowercase"
    elif 'A' <= c <= 'Z':
        return "uppercase"
    elif '0' <= c <= '9':
        return "digit"
    else:
        return "symbol"


if __name__ == "__main__":
    # include corner cases like A and z
    str = "34AfZ`54SDd?za#"
    str.isalpha()
    for c in str:
        # ascii code of c
        # print(ord(c))
        print(f"{c} is a {categorize(c)}")
        # if (isAlpha(c)):
        #     print(f"{c} is an alphabet")
        # if (isNotAlpha(c)):
        #     print(f"{c} is not an alphabet")
