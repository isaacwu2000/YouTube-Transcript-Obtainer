def get_video_id_from_url(video_url):
    from youtube_transcript_api import YouTubeTranscriptApi
    try:
        if "&t=" in video_url:
          video_ID = video_url.split("&")[0]
        video_ID = video_url.split('=')[1]
    except:
        print("An error occured. Please make sure to input a proper url.")
    return video_ID

def get_youtube_transcript(video_id):
    from youtube_transcript_api import YouTubeTranscriptApi
    try:
        # Fetch the transcript for the given video ID
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([entry['text'] for entry in transcript_list])
        return transcript
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
video_url = input("Enter the YouTube video URL: ")
transcript = get_youtube_transcript(get_video_id_from_url(video_url))
print(f"\nTranscript of the video:\n{transcript}")
