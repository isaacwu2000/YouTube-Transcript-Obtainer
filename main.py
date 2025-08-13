import sys
from get_vid_ids import get_channel_vid_ids, get_playlist_vid_ids, get_list_vid_ids
from get_transcripts import get_transcripts

def main():
    if len(sys.argv) != 3:
        raise Exception("Please enter 2 command-line arguements (not including file name).\nRead README.md for more information.")
    match sys.argv:
        case "1": # Channel
            try:
                return channel_transcript(sys.argv[2])
            except Exception as e:
                return e
        case "2": # Playlist
            try:
                return playlist_transcript(sys.argv[2])
            except Exception as e:
                return e
        case "3": # List of video urls
            try:
                return list_of_urls_transcript(sys.argv[2])
            except Exception as e:
                return e
        case _:
            return "Please enter a valid first command-line arguement (not including file name).\nRead README.md for more information."

if __name__ == "__main__":
    print(main())
