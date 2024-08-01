def get_video_title_from_vid_id(vid_id):
    import requests
    from bs4 import BeautifulSoup

    response = requests.get("https://www.youtube.com/watch?v=" + vid_id)
    soup = BeautifulSoup(response.text, "html.parser") 
    title = str(soup.find_all(name="title")[0]).replace("<title>","").replace("</title>","")
    return title

def vid_ids_to_list_of_transcripts(vid_IDs):
    from youtube_transcript_api import YouTubeTranscriptApi

    transcripts_by_vid_title = [] # Format: [{title:transcript}, {title2:transcript}, ...]
    for video_ID in vid_IDs:
        try: # Tests if the video has a transcript to get
            YouTubeTranscriptApi.get_transcript(video_ID)
        except:
            return (f"An error occured in getting the transcript from the video: {get_video_title_from_vid_id(video_ID)}. Please check if the video has a transcript.")
        else:
            youtube_transcript_dict_list = YouTubeTranscriptApi.get_transcript(video_ID)
            youtube_transcript = ""

            # Converts the dictionary transcript (time_in_the_video:text) 
            # into a pure transcript (just text)
            for i in youtube_transcript_dict_list:
                youtube_transcript += " " + str(i["text"])
            transcripts_by_vid_title.append({get_video_title_from_vid_id(video_ID):youtube_transcript})

    return transcripts_by_vid_title

