import sqlite3

conn = sqlite3.connect('myjazzalbums.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

''')

line_count = 0

f = open ("mp3_list.tsv", 'r')

myalbums = []
#print type (myalbums)
for line in f:
    if line_count > 0:
        details = line.split("\t")
        #album  = details[0]
        this_album =  (details[0], details[1])
        myalbums.append(this_album)
        #artist = details [1]
    line_count += 1
        #

bad_flag = False

for entry in myalbums:

    artist = entry[0]
    album = entry[1]
    
    fullstring = artist + ", " + album

    try:
        fullstring.encode('ascii')
    except UnicodeDecodeError:
        bad_flag = True   # string is not ascii
        print fullstring
    else:
        pass  # string is ascii

        if  artist is None or album is None : 
            continue

        #print "creating record: ", artist +": " + album 

        cur.execute('''INSERT OR IGNORE INTO Artist (name) 
            VALUES ( ? )''', ( artist, ) )
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
            VALUES ( ?, ? )''', ( album, artist_id ) )

        conn.commit()

print "complete"
