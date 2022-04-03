import KarlTextParser

with open('textfile.txt', 'r') as f:
    strip = f.read().replace('\n', '')
    print(strip)

import random

with open('textfile.txt') as f:
    lines = f.readlines()
    print(random.choice(lines))


