unzip 20 zip files to the current directory, you will get 20 files:
	20bn-something-something-v2-??
cat 20bn-something-something-v2-?? | tar zx
	this generate 20bn-something-something-v2/
		contain all videos

mkdir annotations
	unzip 20bn-something-something-download-package-labels.zip
		name files as
		something-something-v2-labels.json
		something-something-v2-test.json
		something-something-v2-train.json
		something-something-v2-validation.json
cd ..
python somethingsomethingv2.py --decode_video --build_file_list
	extract mp4 videos to jpg frames, and generate three txt files
	from json annotations files. the txt file rows are "video folder, num frames, action id"

	this runs a long time. default num_threads=100, this is
	actually the number of video files assigned to each thread.
	we actually get 1000s of threads.
	memory not enough. change this value to 10000, now have 20 threads.

python fix_jpegfilename.py
	run this if
	if jpeg file name ######.jpg,

something-something-v2-labels.json:
	class desc, class id

