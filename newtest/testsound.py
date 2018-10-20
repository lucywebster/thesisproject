import simpleaudio as sa

wavObj = sa.WaveObject.from_wave_file("output.wav")
player = wavObj.play()

player.wait_done()
