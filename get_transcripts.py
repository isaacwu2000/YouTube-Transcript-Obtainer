import requests
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi

def get_title(vid_id: str) -> str:
    response = requests.get("https://www.youtube.com/watch?v=" + vid_id)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser") 
    else:
        raise Exception("The webpage data was unable to be retrived.")
    title = str(soup.find_all(name="title")[0]).replace("<title>","").replace("</title>","")
    return title

def get_transcripts(vid_ids: list) -> list:
    ytt_api = YouTubeTranscriptApi()
    transcripts = []
    for vid_id in vid_ids:
        try:
            transcript_with_info = ytt_api.fetch(vid_id)
        except Exception as e:
            return (f"An error occured in getting the transcript from the vid: {get_title(vid_id)}.\nPlease check if the video has a transcript.\nException: {e}")
        else:
            transcript = ""
            for snnipet in transcript_with_info:
                transcript += " " + snnipet.text # Since the transcript also contains time stamps, we extract only the text
            transcripts.append({"title":get_title(vid_id), "transcript":transcript})
    return transcripts