import wave

obj = wave.open("audio.wav", "rb")

print("Number of channels", obj.getnchannels()) #mono, stereo
print("sample width", obj.getsampwidth()) 
print("Frame rate", obj.getframerate()) #Hz e.g. 44,100
print("Number of frames", obj.getnframes())
print("parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/2)

obj.close()

obj_new = wave.open("audio_new.wav","wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)

obj_new.writeframes(frames)

obj_new.close()
