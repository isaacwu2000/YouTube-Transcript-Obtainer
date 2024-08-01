def list_of_vid_ids_from_playlist_url(playlist_url):
    import scrapetube
    playlist_id = playlist_url.split("=")[1]
    video_IDs = []
    for video_dict in scrapetube.get_playlist(playlist_id):
        video_IDs.append(video_dict['videoId'])
    return video_IDs