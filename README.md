# PoetryProject
 
3/31/22
Downloaded Pycharm + Conda
https://quick-adviser.com/how-do-you-randomly-select-a-line-from-a-file-in-python/
Going to try creating a program to pull text from a .txt file

Still unsure of how I want to "house" my program. Should I try and have it run on a website? Should I create a program to run from Pycharm that will be less accessible but will work for my purposes? Embedding a program in a website seems a bit beyond me at this point but the final product would be much better.

https://stackoverflow.com/questions/40844903/how-to-run-python-script-in-html
https://flask.palletsprojects.com/en/2.1.x/
https://www.djangoproject.com/
https://stackoverflow.com/questions/3980059/how-do-i-use-an-external-py-file
https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

https://stackoverflow.com/questions/40140660/print-random-line-from-txt-file
H. REV. comes in clutch with the random line selector. Having trouble still with integrating the text parser, going to ignore this for now.

4/3/21
As part of formatting,  I'm trying to remove line breaks from the text. I am attempting to use `strip(\n)` but keep getting an error saying: `strip = file.strip('\n')
AttributeError: '_io.TextIOWrapper' object has no attribute 'strip`

I think the random print block is working because the f.readLines doesn't need to recognize the text as a string, it just reads directly from the file. I think to strip all \n, the text maybe needs to be imported as a string?

4/7/21
That was not it. I tried a bunch of stuff and forgot to document as I was going but basically what I have now is:

`import random
with open('textfile.txt', 'r+') as f:
    paragraph = f.read().replace('\n',' ')
    string = find_sentences(paragraph)
    print(random.choice(string))`

It successfully parses the text into sentences and prints a random sentence each time. My problem for this was I didn't really know

I'm not quite sure why I got so fixated on parsing text now that I am writing this, though it's definitely a useful feature.

I feel like I should have more to show for my work as of yet but I think I'm starting to get a better grasp on Python as a whole.

I managed to separate the parser from the main and test modules. The `import parser` was greyed out at first because the IDE said it wasn't getting called even though it was, so I changed to `string = parser.find_sentences(paragraph)` and it works now.

I think for reactivity, I will try and have PyAudio detect the peaks of an incoming audio stream and use the peaks to trigger sentence selection.

I collectivized some code from Reddit that prints i/o information using PyAudio functions.
'import pyaudio
p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))'
https://www.reddit.com/r/learnpython/comments/s31hac/does_anyone_use_pyaudio_with_an_external_audio/

I've gained an okayish understanding of how pyaudio works in a basic sense but figuring how to integrate that with arrays from numpy is the next step.

This block gave an error message when starting up a stream saying `fromstring` is deprecated and to use `fromstring` instead to avoid unexpected results, so I made the switch.

`def soundplot(stream):
    t1=time.time()
    data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
    print(data)`


When trying to output text to another txt file, nothing is writing, time to do some research

'with open('input_text.txt', 'r+') as f, open ('output_text.txt', 'r+') as output_text:

    paragraph = f.read().replace('\n',' ')
    string = parser.find_sentences(paragraph)
    output_text.write(random.choice(string))'

FORTUNATELY, it was simply because the output file was named incorrectly. Moving on.
Changed text editing mode to append so previous writes are logged

I found a peak detection algorithm that I am trying to integrate into the 'soundplot()' function in the audio stream module.
the function is 'def __init__(self, array, lag, threshold, influence):' and I cannot figure out what self and array are asking for, and there is no documentation.
There aren't a lot of "readymades" for python realtime peak detection from what I have seen so I will work with this for a little longer before looking more.

Currently I have lag = 30, threshold = 5, and influence as 0. I have array as data which is reading integers from the stream, which is what gets printed to the console. 
Worth noting that I have a pluck routed from Rack to Soundflower and I am getting amplitude information from Rack printed to the console, so at least that works.
Unsure what self even is or what I need to enter for it. Gonna look more into that.

After learning more about arrays, classes and understanding how some of the various peak detection algorithms work, I don't think using actual peak detection is feasible for my knowledge level. 
I think it would be much more reasonable to just have a sentence get selected every time the amplitude of the input signal is greater than a threshold value.

I found a person who created a script that detects "taps" in pyaudio, and it seems to work fairly okay
I've integrated my text selector into the new audio handler, but I can't monitor the output text live, the text updates after the program stops.
I don't think it has to do with changes not being saved while I am viewing the file because using `with open()` should mean the file is closed every write instance.
