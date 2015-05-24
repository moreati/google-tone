#!/usr/bin/env python
"""Generate a Spectrogram image for a given WAV audio sample.

A spectrogram, or sonogram, is a visual representation of the spectrum
of frequencies in a sound.  Horizontal axis represents time, Vertical axis
represents frequency, and color represents amplitude.
"""

import os
import sys

import ewave
import pylab


def graph_spectrogram(wav_file):
    sound_info, frame_rate = get_wav_info(wav_file)
    pylab.figure(num=None, figsize=(8, 6))
    pylab.subplot(111)
    pylab.title('spectrogram of %r' % wav_file)
    pylab.specgram(sound_info, Fs=frame_rate,
                   NFFT=4096, noverlap=4000,
                   )
    pylab.grid(True)
    pylab.axis((0.1, 1.85, 600, 2600))
    pylab.yticks([ 740.0,  830.6,  932.6, 1108.7, 1244.5,
                  1480.0, 1661.2, 1864.66, 2217.46, 2489.0])
    file_name, file_ext = os.path.splitext(wav_file)
    pylab.savefig('%s.%s' % (file_name, 'png'))


def get_wav_info(wav_file):
    wav = ewave.open(wav_file, 'r')
    frames = wav.read()
    #sound_info = pylab.fromstring(frames, 'Int16')
    sound_info = frames
    frame_rate = wav.sampling_rate
    #wav.close()
    return sound_info, frame_rate


def main(argv):
    wav_file = 'sample.wav' if len(argv) <= 1 else argv[1]
    graph_spectrogram(wav_file)

if __name__ == '__main__':
    main(sys.argv)
