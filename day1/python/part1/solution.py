# Advent of Code 2023
# Challenge 1 Part 1
# Aaron Sprouse

calbiration_sum = 0
INPUT_FILE = "input.txt"

with open(INPUT_FILE, "r") as file:
    for row in file:

        buffer = ''

        for i in row:
            if ord(i) in range(48,58):
                buffer += i
                break

        for i in reversed(row):
            if ord(i) in range(48,58):
                buffer += i
                break

        assert len(buffer) == 2

        calbiration_sum += int(buffer)

print(calbiration_sum)