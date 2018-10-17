from speakerphat import clear, show, set_led

clear()
for x in range(10):
    set_led(x,255)
    show()
