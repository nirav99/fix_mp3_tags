"""
Script to add metadata to mp3 file
"""
import argparse
import os
from pathlib import Path
import eyed3
from eyed3.id3.frames import ImageFrame
import sys

def add_tags(audio_file_path: str, artist: str, album: str, title: str, year: str, image_file_path: str):
	"""
	Add the metadata to the given mp3 file.
	The metadata contains artist name, song title, album name, year and the artist image.
	"""

	audiofile = eyed3.load(audio_file_path)
	if audiofile.tag == None:
		audiofile.initTag()

	if image_file_path is not None:
		audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(image_file_path,'rb').read(), 'image/jpeg')

	audiofile.tag.artist = artist
	audiofile.tag.title = title

	if album is not None:
		audiofile.tag.album = album
	audiofile.tag.title = title

	if year is not None:
		audiofile.tag.recording_year = year

	audiofile.tag.save()
	
def is_file_valid(file_name: str, expected_type: str)-> bool:
	"""
	Checks if the given file exists and is of the expected type
	"""
	
	file_path = Path(file_name)
	if file_path.exists() and file_name.lower().endswith("." + expected_type):
		return True
	else:
		return False
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', type=str, help="Name of mp3 file", required=True)
	parser.add_argument('-a', '--artist', type=str, help="Artist name", required=True)
	parser.add_argument('-l', '--album', type=str, help="Album name", required=True)
	parser.add_argument('-t', '--title', type=str, help="Song title", required=True)
	parser.add_argument('-y', '--year', type=str, help="Year", default=None)
	parser.add_argument('-i', '--image', type=str, help="Artist image", default=None)
	args = parser.parse_args()

	params_valid = True

	if is_file_valid(args.file, "mp3") == False:
		print(f"Error. {args.file} is not a valid MP3 file")
		params_valid = False
	else:
		mp3_file = args.file

	if args.image is not None and (is_file_valid(args.image, "jpg") == False):
		print(f"Error: {args.image} is not a valid JPG file")
		params_valid = False

	if args.year is not None and args.year.isdigit() == False:
		print("Error:{args.year} is not a valid number")
		params_valid = False

	if params_valid == False:
		parser.print_help()
		sys.exit(-1)

	add_tags(args.file, args.artist, args.album, args.title, args.year, args.image)

	print("Done...")
	
