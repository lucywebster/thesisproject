
#creating the file to save new recordings to

DATE=$(date +"%Y_%m_%d_%H:%M:S")
arecord --format S16_LE --rate 44100 -c1 sound_$DATE.wav -vv

