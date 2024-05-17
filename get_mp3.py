import argparse
from pytube import YouTube
from moviepy.editor import *
import os

def get_file(url: str):
	print(f"Getting URL : {url}")
	yt = YouTube(url)

	all_streams = yt.streams
	print("All streams")
	print(all_streams)

	# Get the first stream
	first_stream = all_streams.first()

	# Use the first stream to download the file - it will be a video file
	# The file name will be what YouTube returns as song name
	out_file = first_stream.download(output_path="./")
	print("Downloading to file " + out_file)
  
	# Build name for the MP3 file
	base, ext = os.path.splitext(out_file)
	new_file = base + '.mp3'

	# Open the video file, get audio from it and write it as new_file
	# Delete the video file
	video = VideoFileClip(out_file)
	video.audio.write_audiofile(new_file)
	os.remove(out_file)
  
	print(yt.title + " has been successfully downloaded.")
	print("Downloaded file : " + new_file)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', '--url', type=str, help="YouTube URL", required=True)
	args = parser.parse_args()


	get_file(args.url)
