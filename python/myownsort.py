# warm up
# time complexity is O(n^2)
# For n people, numbers of times the outer for loop executes is n.
# For each time outer for loop runs, inner for loop runs n times as well. so total number of steps is n^2
# This means as the number of people grows, the number of greetings (and number of steps the code takes) grows much faster
# — it's quadratic, not linear.
def greeting(people):
    for person1 in people:
        for person2 in people:
            print(f"{person1} says hi to {person2}")


# warm up (additional)
# prints the name of every person in the party.:
# time complexity is O(n)
# For n people, numbers of times the loop executes is n.
# This means as the number of people grows, the number of steps the code takes grows linearly at the same pace.
# this is algorithm that just loops through and prints the name of each person.
def everyPerson(people):
    for person in people:
        print(f"{person} is in the party!")


if __name__ == "__main__":
    people = ["Alex", "Bob", "Charlie", "Dan", "Elaine"]
    everyPerson(people)
    greeting(people)
