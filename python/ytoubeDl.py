from __future__ import unicode_literals
import youtube_dl
from apiclient.discovery import build
from youtube_dl import DownloadError
import sys

sys.modules['win32file'] = None
slozkaSick='C:\\\YTTT\\sick\\'''
slozkaPiratez='C:\\\YTTT\\piratez\\'''
slozkaJa='C:\\\YTTT\\nom\\'''
#import yutubDeadLinksCHecker as ceknito
#loggr = ceknito.yutubDeadLinksCHecker()


ydloptions = {
	'format': 'bestaudio/best',
	#'logger':loggr,
	#'ignoreerrors': True,
	'outtmpl': slozkaPiratez+'%(title)s.%(ext)s',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}

DEVELOPER_KEY = "xxx"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
zjistitoID=False
if not zjistitoID:
	playlistI = youtube.playlistItems().list(
		playlistId="UU1KTo5VQCYzgGMlMvyiffYQ",
		part="snippet",
		maxResults=50
	)


	while playlistI:
		playlistitems_list_response = playlistI.execute()#2requesty
		for playlist_item in playlistitems_list_response["items"]:
			desc = playlist_item["snippet"]["description"]
			tNailurl = playlist_item["snippet"]["thumbnails"]["default"]["url"]
			if not  desc=="This video is unavailable.":
				id = playlist_item["snippet"]["resourceId"]["videoId"]
				title = playlist_item["snippet"]["title"]
				print(title)
				try:
					with youtube_dl.YoutubeDL(ydloptions) as dl:
						dl.download(['http://www.youtube.com/watch?v='+id])
				except DownloadError as dle:
					print ("ERROR: Unable to download info for {url}. It will be skipped. Here is some more info:\n{dle}")
					break
		playlistI = youtube.playlistItems().list_next(playlistI, playlistitems_list_response)



if zjistitoID:
	kanalie = youtube.channels().list(
		forUsername="pirataztek",
		part="contentDetails"
	)

	while kanalie:
		kanalieRespo=kanalie.execute()
		for chanelco in kanalieRespo["items"]:
			uploadsId = chanelco["contentDetails"]["relatedPlaylists"]["uploads"]
			print ("Videos in list %s" % uploadsId)
