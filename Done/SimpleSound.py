import numpy 
import simpleaudio as sa

print("\n")

frequency = int(input("Enter frequency of sound you want to play : "))  
fs = 44100  # 44100 samples per second
seconds = int(input("Enter how long you want the sound to play : "))  
t = numpy.linspace(0, seconds, seconds * fs, False)
note = numpy.sin(frequency * t * 2 * numpy.pi)
audio = note * (2**15 - 1) / numpy.max(numpy.abs(note))
audio = audio.astype(numpy.int16)
play_obj = sa.play_buffer(audio, 1, 2, fs)
play_obj.wait_done()
