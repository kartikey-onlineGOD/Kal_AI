import numpy 
import simpleaudio as sa

print("Hello , I am Kal ,\n I can play any song from the below list for you \n")
print('''1. Attention
2. We don't talk any more
3. Memories
4. Bad Boy''')
ch =int( input("Enter your choice : "))
print('')

if(ch ==1):
    wave_obj = sa.WaveObject.from_wave_file("Assets//Attention.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
elif(ch ==2):
    wave_obj = sa.WaveObject.from_wave_file("Assets//We Don't Talk Anymore.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
elif(ch ==3):
    wave_obj = sa.WaveObject.from_wave_file("Assets//Memories.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
elif(ch ==4):
    wave_obj = sa.WaveObject.from_wave_file("Assets//BadBoy.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()
else:
    print("wrong choice")
    import Songs


    
