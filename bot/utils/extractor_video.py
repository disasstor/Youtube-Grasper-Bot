from pytube import YouTube, Playlist
from bot.utils.extractor_id import get_video_id

regex_num_only = r'^[0-9]*$'


def get_video(id, content_type, url_type):
    if url_type == 'video':
        return get_video_data(id, content_type)
    elif url_type == 'playlist':
        return get_playlist_data(id, content_type)


def get_video_data(id, content_type):
    url = f'https://www.youtube.com/watch?v={id}'
    vid_data_dict = {}
    if content_type == 'audio':
        vid_data = YouTube(url).streams.filter(type='audio', subtype='mp4').desc()
        vid_data_dict = {
            'quality': [i.abr for i in vid_data],
            'itag': [i.itag for i in vid_data],
        }
    elif content_type == 'video':
        vid_data = YouTube(url).streams.filter(type='video', subtype='mp4', progressive=True).desc()
        vid_data_dict = {
            'quality': [i.resolution for i in vid_data],
            'itag': [i.itag for i in vid_data],
        }
    return vid_data_dict


def get_playlist_data(id, content_type):
    url = f'https://www.youtube.com/playlist?list={id}'
    video_urls = Playlist(url).video_urls
    print(video_urls[:1])
    print(video_urls[0])
    return [get_video_data(get_video_id(url)['id'], content_type) for url in video_urls]

