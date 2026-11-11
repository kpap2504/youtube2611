from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix import Channel


url='https://www.youtube.com/@codefirstwithhala/shorts'
channel = Channel(url)

print(f'Channel name: {channel.channel_name}')

video_count = len(channel.videos)
print(f'Number of videos: {video_count}')

if 1==0:
    video_titles = [video.title for video in channel.videos]
    print(f'Video titles: {video_titles}')


if 1==1:
  video_ids =[]
  video_titles = []

  print(f'Downloading videos by: {channel.channel_name}')

  i=0
  for video in channel.videos:
      #download = video.streams.get_highest_resolution().download()
      print(f'Video title: {video.title}')
      i=i+1
      print(i)
      video_ids.append(video.video_id)
      video_titles.append(video.title)

  df = pd.DataFrame({'video_id': video_ids, 'title': video_titles})
  df.to_csv('channel_videos.csv', index=False)    


