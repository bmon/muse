#!/usr/bin/env python3
import numpy as np
import sounddevice as sd

in_device_id = None  # none means default
in_device = sd.query_devices(in_device_id, 'input')
out_device_id = None  # none means default
out_device = sd.query_devices(out_device_id, 'output')

samplerate = in_device['default_samplerate']
low, high = 200, 20000
block_duration = 50  # block duration in ms
best = 0


def callback(indata, outdata, frames, time, status):
    if status:
        print(str(status))

    amplitude = np.sqrt(np.mean(np.square(indata)))  # using rms method
    print('#' * int(amplitude * 100))
    outdata[:] = indata


def main():
    with sd.Stream(
            device=(in_device['name'], out_device['name']),
            samplerate=samplerate,
            blocksize=int(samplerate * block_duration / 1000),
            callback=callback, latency=0):

        # loop
        while True:
            pass


main()
