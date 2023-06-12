import yt_dlp

ydl = yt_dlp.YoutubeDL()

def get_video_infos(url):
    with ydl:
    
            result = ydl.extract_info(
                url,
                download=False
            )
       

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
    return video


def get_audio_url(video):
    for f in video['formats']:
        if f['ext'] == 'm4a':
            return f['url']
    

if __name__ == '__main__':
    video_info = get_video_infos("https://youtu.be/e-kSGNzu0hM")
    url = get_audio_url(video_info)
    print(url)