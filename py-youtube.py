from googleapiclient.discovery import build

#API情報
API_KEY='YOUR_API_KEY'
YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'

youtube=build(
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    developerley=API_KEY
)

search_respose=youtube.search().list(
    q='[vtuber]',
    part='id,snippet',
    maxResults=25
).execute()

channels=[]

for search_result in search_respose.get('items',[]):
    if search_result['id']['kind']=='youtube#channel':
        channels.append([search_result['snippet']['title'],
        search_result['id']['channelId']])

for channel in channels:
    print(channel)