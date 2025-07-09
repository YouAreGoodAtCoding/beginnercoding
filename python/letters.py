# warmup
# python does not have separate char type, they are str of length 1
def isAlphaLib(c: str):
    return c.isalpha()


# if c is an alphabet it should fall between a and z as ascii code is in order
def isAlpha(c: str):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'


if __name__ == "__main__":
    # include corner cases like A and z
    str = "34AfdZ54SDsdgzea#"
    str.isalpha()
    for c in str:
        # ascii code of c
        # print(ord(c))
        if (isAlpha(c)):
            print(f"{c} is an alphabet")
        # if (isAlphaLib(c)):
        #     print(f"{c} is an alphabet (lib function)")
