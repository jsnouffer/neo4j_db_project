from googleapiclient.discovery import build
import pandas as pd

raw_data = {'title': [], 'channelTitle': [], 'tags': []}
df_marks = pd.DataFrame(raw_data)

api_key = 'AIzaSyBJl7cgojKMu0-YDHJW6OWVbjwXWrxaQ7E'

youtube = build('youtube', 'v3', developerKey=api_key)

def getAllVideoData(channelId):
	global df_marks

	vid_ids = []

	ch_request = youtube.channels().list(
		part='snippet, contentDetails, statistics',
		id=channelId
	)

	ch_response = ch_request.execute()

	for item in ch_response['items']:
		mc_playlist_id = item['contentDetails']['relatedPlaylists']['uploads']

	nextPageToken = None
	pl_request = youtube.playlistItems().list(
		part='contentDetails',
		playlistId=mc_playlist_id,
		maxResults=15,
		pageToken=nextPageToken
	)

	pl_response = pl_request.execute()

	for item in pl_response['items']:
		vid_ids.append(item['contentDetails']['videoId'])

	vid_request = youtube.videos().list(
		part="statistics, contentDetails, snippet",
		id=','.join(vid_ids)
	)

	vid_response = vid_request.execute()

	for item in vid_response['items']:
		try:
			new_row = {'title':item['snippet']['title'], 'channelTitle':item['snippet']['channelTitle'], 'tags':item['snippet']['tags']}
		except:
			new_row = {'title':item['snippet']['title'], 'channelTitle':item['snippet']['channelTitle'], 'tags':[]}
		df_marks = df_marks.append(new_row, ignore_index=True)

getAllVideoData('UCe8K2OOoTmpm2u-1ec0fp0Q') # AprilSR
getAllVideoData('UC9HnCqLidC6nLktdUx-WXvA') # TheeSizzler
getAllVideoData('UCtNlOvqfBe8Rue4d7gXj9sQ') # Crafterdark
getAllVideoData('UCl05AQeLaOSjklP8SWpCdgg') # Four
getAllVideoData('UCpkC3VyoQK1zfwciiIYlvfw') # SpeedNintendo
getAllVideoData('UCqMazUQN-db8TmxnrZEA5KA') # k
getAllVideoData('UCTbC5qI5iZa0Q-F4LPla21Q') # Boscarvidios
getAllVideoData('UCcHyxtttXVEp-VaBtKp4wjw') # KaptainWutax
getAllVideoData('UC3AeCFbgCmdSPnQPJduDX3w') # Willz
getAllVideoData('UCv071F-VKI1V_UVVXiuyT-g') # randomidiot13
getAllVideoData('UCuu-Bu1hnwqq0xaK7pZ4OKw') # DKEN
getAllVideoData('UCSqDqnoPqg2VRUs8Jb7OvHw') # Renderedblue
getAllVideoData('UCsntFKaMT0NrGxjtpacC1cg') # pistacium
getAllVideoData('UCUOXKi6Byi57z0iob0bvNwA') # Cubing_Cinematics
getAllVideoData('UCh-nlS-qOHPXkDYYS1e5hEw') # MrMangoHands

df_marks.to_csv(r'D:/MinecraftYoutubeVideoData.csv')
