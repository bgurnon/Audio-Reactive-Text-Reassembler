import random
import parser

def write():
    with open('input_text.txt', 'r') as input_text, open ('output_text.txt', 'a') as output_text:
        paragraph = input_text.read().replace('\n',' ')
        string = parser.find_sentences(paragraph)
        output_text.write(random.choice(string))
        output_text.write('\n')



