import os
 
test = False

if test: 
  #temp path to sample data
  tune_directory = "/Volumes/sandisk2/music/MP3s/jazz"
else: 
  tune_directory = "/Volumes/music/MP3s/jazz"

artist = ""
album = ""
album_list = []

f = open ("mp3_list.tsv", 'w')
f.write ("Artist \t Album" + "\n")

def split_print (instring):
    print ("working")
    sub_paths = instring.split ("/")
    if test:
        sub_paths.remove('sandisk2')
    if len (sub_paths) > 6:
    
        this_album = (sub_paths [5].title(), sub_paths [6].title())
        #print "Artist = " + artist + " Album = "+ album
        #f.write (artist + "\t "+ album + "\n")
        album_list.append(this_album)

def print_tune_files(tune_directory, tune_extensions=['mp3', 'mp4', 'm4a',]):
    ''' Print files in tune_directory with extensions in tune_extensions, recursively. '''
 
    # Get the absolute path of the tune_directory parameter
    tune_directory = os.path.abspath(tune_directory)
    split_print  (tune_directory)
    # Get a list of files in tune_directory
    tune_directory_files = os.listdir(tune_directory)
 
    # Traverse through all files
    for filename in tune_directory_files:
        filepath = os.path.join(tune_directory, filename.lower())
 
        # Check if it's a normal file or directory
        if os.path.isfile(filepath):
 
            # Check if the file has an extension of typical video files
            for tune_extension in tune_extensions:
                # Not a tune file, ignore
                if not filepath.endswith(tune_extension):
                    continue
 
                # We have got a music file! Increment the counter
                #print_tune_files.counter += 1
 
                # Print it's name
                #print('{0}'.format(filepath))
                #f.write('{0}'.format(filepath) + "\n|")
        elif os.path.isdir(filepath):
            # We got a directory, enter into it for further processing
            print_tune_files(filepath)


#print('\n -- Looking for tunes in "{0}" --\n'.format(tune_directory))

# Set the number of processed files equal to zero
#print_tune_files.counter = 0

# Start Processing
print_tune_files(tune_directory)

# We are done. Exit now.
#print('\n -- {0} tune File(s) found in directory {1} --'.format \
#    (print_tune_files.counter, tune_directory))
print ("almost finished")
sorted_list = sorted(album_list)
for albm in sorted_list:
    f.write ( albm[0] + "\t" + albm[1] + "\n")

f.close()