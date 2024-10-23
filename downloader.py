import urllib.request
from shutil import copyfileobj

def download(link):
    video = urllib.request.urlretrieve(link, 'file.mp4')
    return video

