# warmup
def triangle(steps):
    for i in range(0, steps):
        for j in range(0, i+1):
            print("* ", end="")
        print()


def multiplication(end=10):
    for i in range(1, end+1):
        for j in range(1, 11):
            print(i * j, "\t", end="")
        print()


if __name__ == "__main__":
    multiplication(5)
