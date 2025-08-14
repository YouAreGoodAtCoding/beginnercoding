# warm up
# Takes a string and prints how many times each character appears.
def countCharacters(word):
    char_freq = {}
    for char in word:
        char = str.lower(char)
        if (not char.isalpha()):
            continue
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq


def testCountCharacters():
    word = "Hhe;llo!"
    char_freq = countCharacters(word)

    for item, value in char_freq.items():
        print(f"{item}: {value}")


def splitSentenceWithManySpaces(input: str):
    temp_char_arr = []
    result_str_arr = []
    for c in input:
        # we capture only valid characters we care about, ignoring punctuations.
        if (c.isalpha()):
            temp_char_arr.append(c)
        elif (c.isspace()):
            # we flush out only on the first space. remaining spaces are ignored.
            if (len(temp_char_arr) != 0):
                result_str_arr.append(''.join(temp_char_arr))
                temp_char_arr = []

    # need to flush out the chars at the end.
    if (len(temp_char_arr) != 0):
        result_str_arr.append(''.join(temp_char_arr))
        temp_char_arr = []
    return result_str_arr


# main challenge
# Write a program that takes a sentence and prints how many times each word appears.
def countWords(sentence):
    word_freq = {}

    # this split from library handles sentences that has maximum one space
    # and does not ignore punctuations
    # word_arr = sentence.split(" ")

    # out custom split handles sentences that has multiple spaces and ignores punctuations.
    word_arr = splitSentenceWithManySpaces(sentence)
    print(word_arr)
    for word in word_arr:
        word = str.lower(word)
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    for item, value in word_freq.items():
        print(f"{item}: {value}")


def testCountWords():
    # Mixed with punctuations and Upper and lower case.
    sentence = "This is a Test, this  is only a test!"
    countWords(sentence)

    # Empty string.
    sentence = ""
    countWords(sentence)

    # Sentence with repeated words.
    sentence = "hi hi Hi"
    countWords(sentence)

    # All punctuation or numbers.
    sentence = "123 123 !!!"
    countWords(sentence)

    # Only one word.
    sentence = "hello"
    countWords(sentence)

    # Extra spaces.
    sentence = "this     is      spaced"
    countWords(sentence)


if __name__ == "__main__":
    testCountWords()
