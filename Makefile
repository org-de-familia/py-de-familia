# --postprocessor-args "-ss 00:01:00.00 -t 00:00:10.30"
# ffmpeg -i test.mp3 -ss 00:00:20 -to 00:00:40 -c copy -y temp.mp3

get-audio-de-familia:
	youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=Lu5omzcRgCs&ab_channel=VETA2
convert-de-familia:
	mv *.mp3 x.mp3 | exit 0
	ffmpeg -i x.mp3 -ss 00:00:51 -to 00:00:54 -c copy -y out.mp3