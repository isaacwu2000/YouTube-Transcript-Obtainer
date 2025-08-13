import sys
from get_vid_ids import get_channel_vid_ids, get_playlist_vid_ids, get_list_vid_ids
from get_transcripts import get_transcripts

def main():
    if len(sys.argv) != 3:
        raise Exception("Please enter 2 command-line arguements (not including file name).\nRead README.md for more information.")
    try:
        match sys.argv[1]:   
            case "channel": # Channel
                vid_ids = get_channel_vid_ids(sys.argv[2])
            case "playlist": # Playlist
                vid_ids = get_playlist_vid_ids(sys.argv[2])
            case "list": # List of video urls
                vid_ids = get_list_vid_ids(sys.argv[2])
            case _:
                raise Exception("Please enter a valid first command-line arguement (not including file name).\nRead README.md for more information.")
        return get_transcripts(vid_ids)
    except Exception as e:
        return e

if __name__ == "__main__":
    print(main())
