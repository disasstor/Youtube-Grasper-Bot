from pytube import YouTube, Playlist
from bot.utils.extractor_id import get_video_id

regex_num_only = r'^[0-9]*$'


def get_video(id, content_type, url_type):
    if url_type == 'video':
        url = f'https://www.youtube.com/watch?v={id}'
        return get_video_data(id, content_type)
    elif url_type == 'playlist':
        url = f'https://www.youtube.com/playlist?list={id}'
        return get_playlist_data(id, content_type)


def get_video_data(id, content_type):
    url = f'https://www.youtube.com/watch?v={id}'
    if content_type == 'audio':
        vid_data = YouTube(url).streams.filter(type='audio', subtype='mp4').desc()
        vid_data_dict = {}
        abr = []
        itag = []
        for item in vid_data:
            abr.append(item.abr)
            itag.append(item.itag)
        vid_data_dict.update({
            'quality': abr,
            'itag': itag
        })
        return vid_data_dict

    elif content_type == 'video':
        vid_data = YouTube(url).streams.filter(type='video', subtype='mp4', progressive=True).desc()
        vid_data_dict = {}
        res = []
        itag = []
        for item in vid_data:
            res.append(item.resolution)
            itag.append(item.itag)
        vid_data_dict.update({
            'quality': res,
            'itag': itag
        })
        return vid_data_dict


def get_playlist_data(id, content_type):
    url = f'https://www.youtube.com/playlist?list={id}'
    video_urls = Playlist(url).video_urls
    playlist_data = []
    for url in video_urls[:1]:
        playlist_data.append(get_video_data(get_video_id(url)['id'], content_type))
    return playlist_data

