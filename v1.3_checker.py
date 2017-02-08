#!/usr/bin/python
import os, re, eyed3

test = True

if test: 
  top = "/Volumes/sandisk2/music/MP3s"
else: 
  top = "/Volumes/music/MP3s/jazz"

FileTypes=['mp3', 'm4a', 'mp4', 'flac']

cover_found = False

f = open('mp3_log.tsv', 'w')

track_list = dict()

############################################
#  a routine to check the ID3 tag contents 
#
def check_tags (fname):
  audiofile = eyed3.load(fname)
  
  return audiofile.tag.artist, audiofile.tag.album, audiofile.tag.title, audiofile.info.time_secs, audiofile.tag.getBestDate(), str(audiofile.tag.track_num)
  
# end check_tags function code
###########################################

for root, dirs, files in os.walk(top, topdown=False):
    #print "root = ",root
    root_path = root.split("/")
    if not len(root_path) > 7 : continue
    cover_found = False
    genre = root_path [5]
    artist = root_path [6]
    album = root_path [7]
    #f.write ("=================================== \n\n")
    #f.write ("Genre: " + genre + " \n")
    #f.write ("Artist: '" + artist + "' \n")
    #f.write ("No of track: " +  str(len (files)) + " \n")
    f.write ("Artist \t Album \t Trackno \t Title \t ID3_artist \t ID3_album \t ID3_track \t Artist_match \t Album_match \t track_match \n"  )
    for fl in files:
      #print fl
      album_match = True
      artist_match = True
      track_match = True
      
      if fl.lower() == "folder.jpg":
        cover_found = True
      else:
        currentFile=os.path.join(root, fl)
        for FileType in FileTypes:
          if str.endswith(fl,FileType) and not str.startswith(fl, "."):
            print fl
            
            track_no = re.findall('^(\d+).', fl)[0]
            #print " Track No: ", track_no
            track_name = re.findall("\S([a-z A-Z ' \( \)]*)\.\m", fl)[0]
            #print " Track name: ", track_name
            (id_artist, id_album, id_title, id_length, id_date, id_tracknum) = check_tags (currentFile)     
            
            #f.write ("Track " + track_no +": " + track_name +"\n")

            if id_artist.strip().lower() != artist.strip().lower() :
              artist_match = False
              #f.write("Filepath artist doesn't match ID3 Artist: '" + id_artist+ "'\n\n")
            if id_album.strip().lower() != album.strip().lower() :
              album_match = False
              #f.write("Filepath album doesn't match ID3 album: " + id_album+ "\n\n")
            if id_title.strip().lower() != track_name.strip().lower():
              track_match = False 
              #f.write("Filepath track name doesn't match ID3 title: " + id_title+ "\n\n")
            
            f.write(artist + "\t" + album + "\t" + id_tracknum + "\t" + track_name + "\t" + id_artist + "\t" + id_album + "\t" + id_title + "\t" + str(artist_match) + "\t" + str(album_match) + "\t" + str(track_match) + "\n" )
f.close()

