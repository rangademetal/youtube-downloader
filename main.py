from config.test import *
from Download import dl_conv
import os



if __name__ == '__main__':
    print(os.getcwd())
    cmd = PrettyTable(['Command', 'Description'])
    cmd.add_row(['view-all-artist', 'Display all artists'])
    cmd.add_row(['view-all-album', 'Display all artists with albums'])
    cmd.add_row(['find-artist', 'Display artist if he exist in database'])
    cmd.add_row(['find-album', 'Display the artist and album if it exist in database'])
    cmd.add_row(['set-path', 'Set the path'])
    cmd.add_row(['get-path', 'Get the path'])
    cmd.add_row(['download-mp3', 'Download mp3 file with Youtube URL'])
    cmd.add_row(['download-album', 'Download the entire album'])
    print(cmd)
    path = input("Set your path: ")
    os.chdir(path)
    print("Your path is "+path)
    while True:

        ch = input()

        if ch == 'set-path':
            cp = input("Set your path:")
            os.chdir(cp)
        if ch == 'get-path':
            print('Your path is ' + cp)
        if ch == 'view-all-artist':
            get_artist()
        if ch == 'view-all-album':
            get_album()
        if ch == 'find-artist':
            artist = input('Find:')
            artist = artist+'%'
            find_artist(artist)
        if ch == 'find-album':
            album = input('Find:')
            album = album+'%'
            find_album(album)
        if ch == 'download-mp3':
            mp = input("URL:")
            file = input("Enter your file name: ")
            path1 = path+ '/'+file+'.mp4'
            filename = dl_conv.downloaderMp4Youtube(mp, path1)
            path2 = path+ '/'+file+'.mp3'
            dl_conv.Convertor(filename, path2)
        if ch == 'download-album':
            query = input("Enter your album: ")
            os.mkdir(query)

            link_arr = db.getQuery(con, "SELECT sounds.name_sound, sounds.link FROM sounds LEFT JOIN Album ON sounds.id_album = Album.id WHERE Album.album_name = '" + query + "'")
            for i in link_arr:
                path1 = path + '\\' + i[0] + '.mp4'
                filename = dl_conv.downloaderMp4Youtube(i[1], path1)
                path2 = path + '\\' + query + '\\' + i[0] + '.mp3'
                dl_conv.Convertor(filename, path2)