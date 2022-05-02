import pyaudio
import numpy as np
import sys
from peak_detect import real_time_peak_detection
import main

RATE = 44100
CHUNK = int(RATE/20)    # RATE / number of updates per second


def soundplot(stream):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    print(data)


def peaks():
    pd = real_time_peak_detection(np.frombuffer(stream.read(CHUNK), dtype=np.int16), 30, 5, 0)
    print(pd.thresholding_algo(np.frombuffer(stream.read(CHUNK), dtype=np.int16)))


def text():
    main.write_text
    main.write_newline


if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=RATE,
                    input=True,
                    input_device_index=2,
                    frames_per_buffer=CHUNK)
    for i in range(sys.maxsize**10):
        soundplot(stream)
        peaks()
    stream.stop_stream()
    stream.close()
    p.terminate()
