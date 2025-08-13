import requests
from bs4 import BeautifulSoup
from scrapetube import get_channel, get_playlist

def get_channel_vid_ids(channel_url: str) -> str:
    response = requests.get(channel_url)
    if response.status_code == 200:
        source_code = BeautifulSoup(response.text, 'html.parser').prettify()
    else:
        raise Exception("The webpage data was unable to be retrived.")
    channel_id = source_code.split('?channel_id=')[1].split('"',1)[0]
    vid_ids = []
    for vid_dict in get_channel(channel_id):
        vid_ids.append(vid_dict['videoId'])
    return vid_ids

def get_playlist_vid_ids(playlist_url: str) -> list:
    playlist_id = playlist_url.split("=")[1]
    vid_ids = []
    for vid_dict in get_playlist(playlist_id):
        vid_ids.append(vid_dict['videoId'])
    return vid_ids

def get_list_vid_ids(vid_urls: str) -> list:
    vid_urls = vid_urls.split(',')
    vid_ids = []
    for url in vid_urls:
        if '&t=' in url:
            vid_id = url.split("&")[0]
            vid_id = vid_id.split('=')[1]
        else:
            vid_id = url.split('=')[1]
        vid_ids.append(vid_id)
    return vid_ids