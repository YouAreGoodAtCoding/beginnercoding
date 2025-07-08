def count_students_above(scores, threshold):
    cnt = 0
    for score in scores:
        if score > threshold:
            cnt += 1
    return cnt


def print_total_and_average(scores):
    sum = 0
    for score in scores:
        sum += score
    print(f"Sum of all scores is {sum}")
    count = len(scores)
    average = sum / count
    print(f"The average score is: {average}")


def print_highest_score(scores):
    # works for both int and float
    max = float('-inf')
    for score in scores:
        if (score > max):
            max = score
    print(f"The highest score is: {max}")


if __name__ == "__main__":
    scores = [20, 44, 7, 89, 80, 94, 79]
    threshold = 80
    print(f"{count_students_above(scores, threshold)} students scored above {threshold}")
    print_total_and_average(scores)
    print_highest_score(scores)
