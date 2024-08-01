from channel_url_to_vid_ids import *
from list_of_urls_to_vid_ids import *
from playlist_url_to_vid_ids import *
from vid_ids_to_transcript import *

def channel_transcript(channel_url):
    channel_id = get_channel_id_from_url(channel_url)
    vid_ids = list_of_vid_ids_from_channel_id(channel_id)
    return vid_ids_to_list_of_transcripts(vid_IDs)
def playlist_transcript(playlist_url):
    vid_ids = list_of_vid_ids_from_playlist_url(playlist_url)
    return vid_ids_to_list_of_transcripts(vid_IDs)
def list_of_urls_transcript(list_of_urls):
    vid_ids = get_list_of_vid_ids_from_list_of_urls(list_of_vid_urls)
    return vid_ids_to_list_of_transcripts(vid_IDs)

def main():
    import sys
    # The first sys arguement should be:
        # '1' for a transcript of all of a channels videos
        # '2' for a transcript of all of a playlists videos
        # '3' for a transcript of all of the videos in a list of urls
    # The second sys arguement should be:
        # The channel/playlist url if the first arg was 1 or 2
        # The list of video urls in the format: video_url1, video_url2, ... | if the first arg was 3
    
    # Checking that there are exactly 3 command-line args (2 excluding the file name)
    if len(sys.argv) != 3:
        return "Please enter 2 command-line arguements (not including file name). Read README.md for more information."
    
    if sys.argv[1] == 1: # Channel
        try:
            return channel_transcript(sys.arv[2])
        except Exception as e:
            return e
    elif sys.argv[1] == 2: # Playlist
        try:
            return playlist_transcript(sys.arv[2])
        except Exception as e:
            return e
    elif sys.argv[1] == 3: # List of video urls
        try:
            return list_of_urls_transcript(sys.arv[2])
        except Exception as e:
            return e
    else:
        return "Please enter a valid first command-line arguement (not including file name). Read README.md for more information.
    


if __name__ == "__main__":
    print(main())