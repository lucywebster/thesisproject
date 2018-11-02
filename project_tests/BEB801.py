#!/usr/bin/env python
#
# The following program has been written by Lucy Webster, 09154752, for the purpose of 
# BEB801 Project, Intergenerational Language Transmission at QUT
#
# The file will allow read and write on to RFID cards

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True
card_empty = False


# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        print "\n"
# Check if authenticated
        if status == MIFAREReader.MI_OK:

            print "The card look like this:"
            # Read block 8
            if MIFAREReader.MFRC522_Read(8) == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
                card_empty = True
                continue_reading = False
                # Stop
                MIFAREReader.MFRC522_StopCrypto1()
            else:
                #Make some sounds
                if status == MIFAREReader.MI_OK:
                   data = MIFAREReader.MFRC522_Read(8)
                   text = "".join(chr(x) for x in data)
                   print text
                   continue_reading = False
        else:
            print "Authentication error"

if card_empty:
    name = raw_input("Enter a Card Name:")
    if len(name)>16:
        name=name[:16]
    data = [ord(x) for x in list(name)]

while card_empty:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
        print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
    
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
        print "\n"
# Check if authenticated
        if status == MIFAREReader.MI_OK:

            # Variable for the data to write
#            data = []

            # Fill the data with 0xFF
            for x in range(0,16):
                data.append(0xFF)

            print "The card looked like this:"
            # Read block 8
            MIFAREReader.MFRC522_Read(8)
            print "\n"

            # Write the data
            MIFAREReader.MFRC522_Write(8, data)
            print "\n"

            print "It now looks like this:"
            # Check to see if it was written
            MIFAREReader.MFRC522_Read(8)
            print "\n"

            # Stop
            MIFAREReader.MFRC522_StopCrypto1()

            # Make sure to stop reading for cards
            card_empty = False
