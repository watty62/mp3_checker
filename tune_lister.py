import os, eyed3
 
test = True

if test: 
  #temp path to sample data
  tune_directory = "/Volumes/sandisk2/music/MP3s/jazz"
else: 
  tune_directory = "/Volumes/music/MP3s/jazz"

artist = ""
album = ""
album_list = []
tune_count = 0

f = open ("tuneslist.tsv", 'w')
f.write ("Filepath \t Artist \t Album \t tune" + "\n")

def id3_process (instring):


def split_print (instring):
    #print ("working")
    sub_paths = instring.split ("/")
    if test:
        sub_paths.remove('sandisk2')

    if len (sub_paths) > 6:
        
        this_album = (sub_paths [5].title(), sub_paths [6].title())
        
        return this_album

def print_tune_files(tune_directory, tune_extensions=['mp3', 'mp4', 'm4a','flac']):
    ''' Print files in tune_directory with extensions in tune_extensions, recursively. '''
 
    # Get the absolute path of the tune_directory parameter
    tune_directory = os.path.abspath(tune_directory)
    details = split_print  (tune_directory)
    

    # Get a list of files in tune_directory
    tune_directory_files = os.listdir(tune_directory)
    
    # Traverse through all files
    for filename in tune_directory_files:
        filepath = os.path.join(tune_directory, filename.lower())
        
        # Check if it's a normal file or directory
        if os.path.isdir(filepath):
            # We got a directory, enter into it for further processing
            print_tune_files(filepath)
        else: 
            # "it's a file"
            for ext in tune_extensions:
                if filepath.endswith(ext):
                    tune = filepath.split('/')[-1]
                    
                    f.write (filepath + "\t" + details[0] +"\t" + details[1] + "\t" + tune + "\n")
                    id3_process(filepath)

                    tune += 1
                    
#print('\n -- Looking for tunes in "{0}" --\n'.format(tune_directory))

# Start Processing
print_tune_files(tune_directory)

# We are done. Exit now.
#print('\n -- {0} tune File(s) found in directory {1} --'.format \
#    (print_tune_files.counter, tune_directory))

sorted_list = sorted(album_list)
for albm in sorted_list:
    f.write ( albm[0] + "\t" + albm[1] + "\n")

f.close()

print "Number of tunes found = " + str(tune_count)
