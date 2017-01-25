#!/usr/bin/python
import os, re, eyed3

test = True

if test: 
  #temp path to sample data
  top = "/Volumes/sandisk2/music/MP3s"
else: 
  top = "/Volumes/music/MP3s/jazz"

FileTypes=['mp3', 'm4a']

cover_found = False

f = open('mp3_log.txt', 'w')

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
    f.write ("=================================== \n")
    f.write ("Genre: " + genre + " \n")
    f.write ("Artist: " + artist + " \n")
    f.write ("Genre: " + genre + " \n")
    f.write ("No of track: " +  str(len (files)) + " \n")

    for fl in files:
      #print fl
      if fl.lower() == "folder.jpg":
        cover_found = True
      else:
        currentFile=os.path.join(root, fl)
        for FileType in FileTypes:
          if str.endswith(fl,FileType):
            
            track_no = re.findall('^(\d+).', fl)[0]
            #print " Track No: ", track_no
            track_name = re.findall("\S([a-z A-Z ' \( \)]*)\.\m", fl)[0]
            #print " Track name: ", track_name
            (id_artist, id_album, id_title, id_length, id_date, id_tracknum) = check_tags (currentFile)     

            f.write ("Track " + track_no +": " + track_name +"\n \n")

            if id_artist != artist :
              f.write("Artist doesn't match: " + id_artist+ "\n")
            if id_album != album :
              f.write("Album doesn't match: " + id_album+ "\n")
            if id_title != track_name :
              f.write("Track name doesn't match: " + id_title+ "\n")

f.close()

