from io import BytesIO
from urllib.request import urlopen
from PIL import Image
from aiogram.types import InputFile
from pytube import YouTube, Playlist


def get_thumb(id: str, type: str, form: str = 'square') -> InputFile:
    thumb_url = get_thumb_url(id, type)
    return get_thumb_buffer(thumb_url, form)


def get_thumb_url(id: str, type: str) -> str:
    if type == 'video':
        url = f'https://www.youtube.com/watch?v={id}'
        return YouTube(url).thumbnail_url
    elif type == 'playlist':
        url = f'https://www.youtube.com/playlist?list={id}'
        return YouTube(Playlist(url).video_urls[0]).thumbnail_url


def get_thumb_buffer(media_thumb_url: str, form: str) -> InputFile:
    form_dict = {'square': 0, 'circle': 110}
    image = Image.open(urlopen(media_thumb_url), 'r')
    side = image.height - form_dict.get(form)
    image = crop_center(image, side)
    bytes_io = BytesIO()
    image.save(bytes_io, format='JPEG')
    bytes_io.seek(0)
    return InputFile(bytes_io, filename='thumbnail.jpg')


def crop_center(pil_img: Image, crop_side: int) -> Image:
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_side) // 2,
                         (img_height - crop_side) // 2,
                         (img_width + crop_side) // 2,
                         (img_height + crop_side) // 2))
