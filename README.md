# mp3_checker
checking mp3 library file names and ID3 tags

This is a work in progress. 

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
