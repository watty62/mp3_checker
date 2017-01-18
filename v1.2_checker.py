
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
  print "******************"
  print "Data from ID3 tags"
  
  print " Artist: %s" % audiofile.tag.artist
  print " Album: %s" % audiofile.tag.album
  print " Track: %s" % audiofile.tag.title
  print " Track Length: %s" % audiofile.info.time_secs
  print " Release Year: %s" % audiofile.tag.getBestDate()
  print " Track Number: %s" % str(audiofile.tag.track_num)
  print ""
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
            
            track_no = re.findall('^(\d+).', fl)
            print " Track No: ", track_no
            track_name = re.findall("\S([a-z A-Z ' \( \)]*)\.\m", fl)
            print " Track name: ", track_name
            check_tags (currentFile)
              


