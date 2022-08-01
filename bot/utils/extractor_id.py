import re
regex_youtube = r'(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?'
regex_video_id = r'^.*(youtu.be\/|watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})'
regex_playlist_id = r'^.*(youtu.be\/|list=)(?P<id>[^#\&\?]{34})'
#regex_video_id = r'^.*(youtu.be\/|watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})'
#regex_playlist_id = r'^.*(youtu.be\/|list=)(?P<id>[^#\&\?]*).*'

def get_id(url):
    if re.match(regex_playlist_id, url):
        return get_playlist_id(url)
    elif re.match(regex_video_id, url):
        return get_video_id(url)
    else:
        return None


def get_video_id(url):
    id_video = re.match(regex_video_id, url).group('id')
    return {'type': 'video', 'id': id_video}


def get_playlist_id(url):
    id_playlist = re.match(regex_playlist_id, url).group('id')
    return {'type': 'playlist', 'id': id_playlist}
