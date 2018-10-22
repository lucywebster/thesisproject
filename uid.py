import RPi.GPIO as GPIO
import MFRC522 
import signal
import SimpleMFRC522
from time import sleep

#continue_reading = True

#def end_read(signal,frame):
 #   global continue_reading
  #  print ("start")
   # continue_reading = False
   # GPIO.cleanup()

#signal.signal(signal.SIGINT, end_read)

MIFAREReader = MFRC522.MFRC522()

reader = SimpleMFRC522.SimpleMFRC522()

file = open("uid.txt","a")

print("Read atg")

try:
    while True:
    
    #(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    
    #(status,uid) = MIFAREReader.MFRC522_Anticoll()

    #if status == MIFAREReader.MI_OK:

        #print("Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2],uid[3]))

        id, text = reader.read()
        #print(text)

        file.write(str(id)+"\n")
        sleep(1)
except KeyboardInterrupt:
        print("cleaning up")
        GPIO.cleanup()
        file.close()
