""" Count how many numbers from 1–100 are divisible by 7
"""

count = 0
# stop is exclusive, so we go up to 101
for i in range(1, 101):
    if (i % 7 == 0):
        count += 1


print(f"There are {count} numbers divisible by 7 between 1 to 100")
