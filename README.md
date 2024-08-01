# YouTube-Transcript-Obtainer
Obtains a transcript(s) of all the YouTube videos from a channel URL, a playlist URL,\
or a list of video URLs using *ScrapeTube* (https://pypi.org/project/scrapetube/), \
*Youtube-Transcript-API* (https://pypi.org/project/youtube-transcript-api/), \
and *BeautifulSoup4* (https://pypi.org/project/beautifulsoup4/).

### Usage Guide:
Run main.py with 2 command-line arguements:\
(Ignore the filename as a command-line arguement for these instructions)

The first command-line arguement should be:\
&emsp;- '1' for a transcript of all of a channels videos\
&emsp;- '2' for a transcript of all of a playlists videos\
&emsp;- '3' for a transcript of all of the videos in a list of urls
    
The second command- line arguement should be:\
&emsp;- If the first arg was 1 or 2, the channel/playlist url \
&emsp;- If the first arg was 3, the list of video urls in the format: "video_url1, video_url2, ..."\
&emsp;(The quotations are neccesary) 
