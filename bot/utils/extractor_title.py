from pytube import YouTube, Playlist


def get_title(id, type):
    if type == 'video':
        url = f'https://www.youtube.com/watch?v={id}'
        return YouTube(url).title
    elif type == 'playlist':
        url = f'https://www.youtube.com/playlist?list={id}'
        return YouTube(Playlist(url).video_urls[0]).title