
import random
import parser

with open('textfile.txt', 'r+') as f:

    paragraph = f.read().replace('\n',' ')
    string = parser.find_sentences(paragraph)
    print(random.choice(string))

