# Audio-Based Text Reassembler

### Summary
My final product is a collection of modules that work together to:
- parse a text input into sentences
- analyze the amplitude of an audio input in 'realtime'
- detect high amplitude, short decay sections
- use those detected 'taps' to trigger to write a sentence to an output text file that can be viewed in realtime

### Text Handling
I began the project working on writer.py, which used functions from parser.py to parse text from input_text.txt and print a random sentence to the console. I later modified the module to write to output_text.txt for realtime monitoring in Atom.
writer.py was based off of the work of H. Rev. on StackOverflow *[here](https://stackoverflow.com/questions/40140660/print-random-line-from-txt-file)*.
parser.py was written by TennisVisuals on StackOverflow *[here](https://stackoverflow.com/questions/4576077/how-can-i-split-a-text-into-sentences)*.

### Audio Handling
For the audio stream portion of the program, I learned the basics of initiating an audio stream using Pyaudio, but the next steps of processing the audio stream from scratch would have required too much time for the deadline. Learning and integrating numpy or scipy peak finding algorithms was too much of a learning curve for the timeframe, plus I wasn't sure if the results would have been viable anyways. I was lucky enough to find some code made by Russell Borogove on StackOverflow *[here](https://stackoverflow.com/questions/4160175/detect-tap-with-pyaudio-from-live-mic)* that was created to detect taps on a microphone to trigger some other event in a live setting.
I am using a shortened, edited version of this code made by user1405612.

tap_detect.py breaks up an incoming audio stream into blocks and calculates the rms amplitude of each block. Based off of a threshold set by the user, the program will determine each incoming block as either loud or quiet, and it will register a "tap" if a certain number of loud blocks are followed by a certain number of quiet blocks. If there are too many loud or quiet blocks being registered, the threshold will be multiplied by 1.1 or 0.9 respectively to increase or decrease sensitivity. I integrated writer.py by calling write() whenever a tap is registered. The last element is io_check.py which is more a less a standalone module that I use to list the input devices for use in setting up tap_detect.py.

### Problems I Faced
Something that took me a while to figure out early on was how to correctly call functions from imported local modules. I found out after a while that the function needs to be called like `module.function`.

One dumb problem I faced was not realizing that in my writer function, I had the wrong .txt file name in `open()`. Understanding the read/write modes took a while as well.

A significant issue that I could not figure out was how to even integrate and use delica's peak detection algorithm from StackOverflow *[here](https://stackoverflow.com/questions/48653745/continuesly-streaming-audio-signal-real-time-infinitely-python)*. The lack of documentation combined with my basic understanding of Python resulted in me not knowing how to even use the functions provided. I still don't fully understand classes and `self`, nor do I fully understand arrays and how they are used in terms of signals like audio. These are points of interest for progressing in Python.

The final issue I faced was live monitoring output_text.txt because Pycharm only refreshes files when moving between files. Most text and document viewers are the same, and this led me down the rabbit hole of log followers and niche software that seems to only exist for Windows and Linux. Fortunately, I discovered the Atom does auto-refresh and this is what I recommend for monitoring output_text.txt.

### Closing
While this program didn't meet my original expectations, that is because my original expectations were far too lofty. Some things I would potentially like to improve in the future are the audio processing, and I also think even a simple user interface would make this far more accessible.
