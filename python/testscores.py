def count_students_above(scores, threshold):
    count = 0
    for score in scores:
        if score > threshold:
            count += 1
    return count


if __name__ == "__main__":
    scores = [20, 44, 7, 89, 80, 94, 79]
    threshold = 80
    print(f"{count_students_above(scores, threshold)} students scored above {threshold}")
