import simpleaudio as sa

wavObj = sa.WaveObject.from_wave_file("recordtest.wav")
player = wavObj.play()

player.wait_done()
