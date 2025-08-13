# YouTube-Transcript-Obtainer
Obtains a transcript(s) of all the YouTube videos from a channel URL, a playlist URL,\
or a list of video URLs

### Usage Guide:
To set the neccesary (to protect your IP) Webshare proxy, create an environemental variable ```proxy-username=your-webshare-proxy-username```
```proxy-password=your-webshare-proxy-password```

Run main.py with 2 command-line arguements:\
(Ignore the filename as a command-line arguement for these instructions)

The first command-line arguement should be:\
* 'channel' for a transcript of all of a channel's videos\
* 'playlist' for a transcript of all of a playlist's videos\
* 'list' for a transcript of all of the videos in a list of url(s) or a single video
    
The second command- line arguement should be:\
* If the first arg was 1 or 2, the channel/playlist url \
* If the first arg was 3, the list of video urls in the format: "video_url1, video_url2, ..." (Note that the quotations are neccesary)

The transcripts will then be written to ```transcripts.json```