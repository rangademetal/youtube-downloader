from Database import Database
from prettytable import PrettyTable


host = 'hosting1993073.online.pro'
user = '00286862_youtubedownloader'
password = 'youtubedownloader'
database = '00286862_youtubedownloader'

db = Database.Database(host=host, user=user, password=password, database=database)
con = db.connection()

def get_artist():
    artist = db.getQuery(con, 'SELECT ARTIST.artist_name FROM ARTIST')
    t = PrettyTable(['Artist'])
    for i in artist:
        t.add_row([i[0]])
    print(t)


def get_album():
    album = db.getQuery(con,'SELECT ARTIST.artist_name, Album.album_name FROM ARTIST LEFT JOIN '
                            'Album ON ARTIST.id = Album.id_artist ')
    al = PrettyTable(['Artist', 'Album'])
    for i in album:
        al.add_row([i[0],i[1]])
    print(al)



def get_album_and_sounds(artist):
    query = db.getQuery(con, "SELECT Album.album_name, sounds.name_sound FROM Album LEFT JOIN sounds ON sounds.id_album = Album.id LEFT JOIN ARTIST ON ARTIST.id = Album.id_artist where ARTIST.artist_name = '"+str(artist)+"'")
    t = PrettyTable(['Album', 'Sound'])
    for i in query:
        t.add_row([i[0], i[1]])
    print(t)


def find_artist(find):
    found_artist = db.getQuery(con, "SELECT ARTIST.artist_name FROM ARTIST WHERE ARTIST.artist_name Like '"+str(find)+"'")
    t = PrettyTable(['Artist'])
    for i in found_artist:
        t.add_row([i[0]])
    print(t)


def find_album(find):
    found_album = db.getQuery(con, "SELECT Album.album_name FROM Album WHERE Album.album_name Like '"+str(find)+"'")
    t = PrettyTable(['Artist'])
    for i in found_album:
        t.add_row([i[0]])
    print(t)