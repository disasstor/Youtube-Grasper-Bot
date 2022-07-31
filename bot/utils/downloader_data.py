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
    data = youtube.streams.get_by_itag(itag)
    title = data.title
    author = youtube.author
    thumbnail = youtube.thumbnail_url
    filename = data.default_filename
    video_data = [title, author, thumbnail, filename, id]
    return video_data


def get_playlist_data(id, itag):
    url = f'https://www.youtube.com/playlist?list={id}'
    urls = Playlist(url).video_urls
    playlist_data = []
    for url in urls:
        playlist_data.append(get_video_data(get_video_id(url)['id'], itag))
    return playlist_data

