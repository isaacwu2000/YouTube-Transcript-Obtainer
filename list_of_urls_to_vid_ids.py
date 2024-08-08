def get_list_of_vid_ids_from_list_of_urls(list_of_vid_urls):
    list_of_vid_urls = list_of_vid_urls.split(',') # Converts the inputted comma-seperated list of URLs into a python list
    video_IDs = []
    for url in list_of_vid_urls:
        if '&t=' in url:
            vid_ID = url.split("&")[0]
            vid_ID = vid_ID.split('=')[1]
        else:
            vid_ID = url.split('=')[1]
        video_IDs.append(vid_ID)
    return video_IDs
