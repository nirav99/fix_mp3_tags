# fix_mp3_tags
Allows the user to specify different meta data values in MP3 file such as artist name, song title, album name, year and the artist image.
The artist image and the year are optional, rest of the parameters must be specified.
________

### Setup
Make sure you are using python3
```bash
python3 --version
```
should return 3.7+
then install dependencies

```bash
pip3 install -r requirements.txt
```
________

### Usage

```bash
python fix_mp3_metadata.py -h  
usage: fix_mp3_metadata.py [-h] [-f FILE] [-a ARTIST] [-l ALBUM] [-t TITLE]
                           [-y YEAR] [-i IMAGE]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Name of mp3 file
  -a ARTIST, --artist ARTIST
                        Artist name
  -l ALBUM, --album ALBUM
                        Album name
  -t TITLE, --title TITLE
                        Song title
  -y YEAR, --year YEAR  Year
  -i IMAGE, --image IMAGE
                        Artist image
```

________
