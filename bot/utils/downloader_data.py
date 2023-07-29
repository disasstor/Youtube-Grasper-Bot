from pytube import YouTube, Playlist

from bot.utils.extractor_id import get_video_id


def get_data(id, itag, url_type):
    if url_type == 'video':
        return [get_video_data(id, itag)]
    elif url_type == 'playlist':
        return get_playlist_data(id, itag)


def get_video_data(id, itag):
    url = f'https://www.youtube.com/watch?v={id}'
    youtube = YouTube(url)
    stream_data = youtube.streams.get_by_itag(itag)
    return [stream_data.title, youtube.author, youtube.thumbnail_url, stream_data.default_filename, id]


def get_playlist_data(id, itag):
    url = f'https://www.youtube.com/playlist?list={id}'
    urls = Playlist(url).video_urls
    return [get_video_data(get_video_id(url)['id'], itag) for url in urls]

