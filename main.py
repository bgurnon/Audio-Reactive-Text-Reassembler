import random

with open('textfile.txt', 'r') as f:
    strip = f.read().replace('\n', '')
    print(strip)

with open('textfile.txt') as f:
    lines = f.readlines()
    rand_line = random.randint(0, len(lines) - 1)
    print(lines[rand_line])


