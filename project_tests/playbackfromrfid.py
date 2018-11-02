import simpleaudio as sa
import RPi.GPIO as GPIO
import MFRC522
import signal
import SimpleMFRC522
from time import sleep

f = open("record.txt","w")
reader = SimpleMFRC522.SimpleMFRC522()


print("Scan Tag!")

try:
    while True:
        
        id,text = reader.read()
        
        search = "{0}.wav".format(str(id))
        print("Playing "+search)

        wavObj = sa.WaveObject.from_wave_file(search)
        player = wavObj.play()

        player.wait_done()

except KeyboardInterrupt:
    print("Finsih!")
    GPIO.cleanup()
    file.close()
