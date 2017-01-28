# mp3_checker
checking mp3 library file names and ID3 tags

This is a work in progress (2017-Jan-28)

At the moment I have two working routines: 
* album_lister2.py which traverses the directory structure, extracts artist name and ablum name and writes those to a TSV file (I avoided CSV as several album titles contain commas), and
* update_db.py which reads the TSV file and processes the contents. If Sthe QLite database does not exist it creates one. It reads line by line (and traps any non-standard characters - printing those out for correction) then checks if the artist exists, if not creates one, then inserts the album into the database.

I wanted to complete this functionality so that I can use the database for a Jazz Bot project. 

I intend to come back and complete everthing else, below.

Requirements 
The eyed3 module - "sudo pip install eyed3"

Its function will be 

* to walk through a very large collection of MP3 (and other music fomat) files
* derive from the directory structure and file name the genre, artist, album, song, song number
* read the ID3 tags for those same tags as well as length, running order, year (and maybe some more) 
* check if a folder.jpg exists for each album
* Log all of this to a SQLite database, and for easy access a flatfile CSV

I want it to highlight missing or contradictory tagging for later correction

I might make it fix missing tags and grab folder.jpg images from somewhere.

Latest (limited working) version is V1.3
