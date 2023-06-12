import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

FRAMES_PER_BUFFER = 3200
CHANNELS = 1
RATE = 16000
SECONDS = 5

# Create a stream
stream = sd.InputStream(
    samplerate=RATE,
    channels=CHANNELS,
    blocksize=FRAMES_PER_BUFFER,
    dtype='int16'
)

print("start recording")

frames = []
with stream:
    for _ in range(0, int(RATE/FRAMES_PER_BUFFER*SECONDS)):
        frame = stream.read(FRAMES_PER_BUFFER)
        frames.append(frame[0])

print("recording ended")

# Save to file
frames = np.concatenate(frames)  # Join the frames together
wav.write("output.wav", RATE, frames)
