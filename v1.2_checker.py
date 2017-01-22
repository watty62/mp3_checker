
import os, re, eyed3

#temp path to sample data
top = "/Volumes/sandisk2/music/MP3s"

FileTypes=['mp3', 'm4a']

cover_found = False
#trax =dict()

############################################
#  a routine to check the ID3 tag contents 
#
#  to be amended to return tag values
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
    print "================================"
    print "New Album"
    print "================================"
    print "Data generated from path hierarchy"
    print " genre = ", genre
    print " artist = ", artist
    print ' album = ', album
    print " number of files =", len(files)
    
    for fl in files:
      #print fl
      if fl.lower() == "folder.jpg":
        cover_found = True
      else:
        currentFile=os.path.join(root, fl)
        for FileType in FileTypes:
          if str.endswith(fl,FileType):
            
            track_no = re.findall('^(\d+).', fl)[0]
            print " Track No: ", track_no
            track_name = re.findall("\S([a-z A-Z ' \( \)]*)\.\m", fl)[0]
            print " Track name: ", track_name
            (id_artist, id_album, id_title, id_length, id_date, id_tracknum) = check_tags (currentFile)
            print id_artist
            print id_album
            print id_title
            print id_length
            print id_date
            print id_tracknum

'''
print "Compare with ID3 tags"
  
  if audiofile.tag.artist != artist:
    print " Artist doesn't match: ", audiofile.tag.artist
  else:
    print " Artist  matches"
  if audiofile.tag.album != album:
    print " Album doesn't match: ", audiofile.tag.album
  else:
      print " Album matches"
  if audiofile.tag.title != track_name:
    print " Track name doesn't match: ", audiofile.tag.title
  else:
    print " Track name matches"

  print "***********************"
  '''
