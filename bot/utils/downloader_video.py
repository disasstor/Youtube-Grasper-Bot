import threading
from pytube import YouTube, Playlist


def worker(url, itag):
    yt = YouTube(url).streams.get_by_itag(itag)
    yt.download()
    print(yt.title)


def downloader(id, url_type, itag):
    urls = []
    if url_type == 'video':
        url = f'https://www.youtube.com/watch?v={id}'
        urls.append(url)
    elif url_type == 'playlist':
        url = f'https://www.youtube.com/playlist?list={id}'
        urls = Playlist(url).video_urls
    complited = 0
    for url in urls:
        thread = threading.Thread(target=worker, args=(url, itag), daemon=True)
        thread.start()
        thread.join()
        complited += 1
        if complited == len(urls):
            return True



