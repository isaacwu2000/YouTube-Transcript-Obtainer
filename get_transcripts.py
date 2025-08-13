import requests
import json
import random
import os
import time
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
from dotenv import load_dotenv

def get_title(vid_id: str) -> str:
    response = requests.get("https://www.youtube.com/watch?v=" + vid_id)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser") 
    else:
        raise Exception("The webpage data was unable to be retrived.")
    title = str(soup.find_all(name="title")[0]).replace("<title>","").replace("</title>","")
    return title

def write_to_json(transcript: dict):
    print('d')
    with open("transcripts.json", 'r+') as file:
        print('e')
        file_data = json.load(file)
        file_data.append(transcript)
        print('f')
        json.dump(file_data, file, indent=4)

def write_transcripts(vid_ids: list):
    from youtube_transcript_api.proxies import GenericProxyConfig
    load_dotenv()
    ytt_api = YouTubeTranscriptApi(
        proxy_config=WebshareProxyConfig(
            proxy_username=os.environ["proxy-username"],
            proxy_password=os.environ["proxy-password"],
        )
    )
    transcripts = []
    for vid_id in vid_ids:
        try:
            transcript_with_info = ytt_api.fetch(vid_id)
            transcript = ""
            for snnipet in transcript_with_info:
                transcript += " " + snnipet.text # Since the transcript also contains time stamps, we extract only the text
            write_to_json({"title":get_title(vid_id), "transcript":transcript})
        except Exception as e:
            print(e)    
            quit()        
        time.sleep(random.random())
        