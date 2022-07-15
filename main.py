from pytube import Playlist
youtube_playlist_link = "add_your_playlist_link_here"
playlist = Playlist(youtube_playlist_link)
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video in playlist.videos:
    video.streams.first().download()