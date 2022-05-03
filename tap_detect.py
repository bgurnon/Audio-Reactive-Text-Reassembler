import pyaudio
import struct
import math
import writer

INITIAL_TAP_THRESHOLD = 0.01
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
INPUT_DEVICE_INDEX = 11
CHANNELS = 1
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)

OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME

UNDERSENSITIVE = 150.0/INPUT_BLOCK_TIME  # if we get this many quiet blocks in a row, decrease the threshold

MAX_TAP_BLOCKS = 80.0/INPUT_BLOCK_TIME  # if the noise was longer than this many blocks, it's not a 'tap'


def get_rms(block):

    # RMS amplitude is defined as the square root of the 
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into 
    # a string of 16-bit samples...

    # we will get one short out for each 
    # two chars in the string.
    count = len(block)/2
    format = "%dh" % count
    shorts = struct.unpack(format, block)

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768.
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt(sum_squares / count)


pa = pyaudio.PyAudio()

stream = pa.open(format=FORMAT,                      #|
                 channels=CHANNELS,                          #|---- You always use this in pyaudio...
                 rate=RATE,                                  #|
                 input=True,                                 #|
                 input_device_index=INPUT_DEVICE_INDEX,      #] sets audio input
                 frames_per_buffer=INPUT_FRAMES_PER_BLOCK)   #]

tap_threshold = INITIAL_TAP_THRESHOLD                  #]
noisycount = MAX_TAP_BLOCKS+1                          #|---- Variables for noise detector...
quietcount = 0                                         #|
errorcount = 0                                         #]         

for i in range(10000):
    try:                                                    #]
        block = stream.read(INPUT_FRAMES_PER_BLOCK)         #|
    except IOError as e:                                      #|---- just in case there is an error!
        errorcount += 1                                     #|
        print("(%d) Error recording: %s" % (errorcount, e))  #|
        noisycount = 1                                      #]

    amplitude = get_rms(block)
    if amplitude > tap_threshold:       # if its to loud...
        quietcount = 0
        noisycount += 1
        if noisycount > OVERSENSITIVE:
            tap_threshold *= 1.1        # turn down the sensitivity

    else:    # if it's too quiet...

        if 1 <= noisycount <= MAX_TAP_BLOCKS:
            writer.write()      # triggers sentence selection
            print('tap')
        noisycount = 0
        quietcount += 1

        if quietcount > UNDERSENSITIVE:
            tap_threshold *= 0.9     # turn up the sensitivity
