from django.shortcuts import render
from apiclient.discovery import build
# Create your views here.
api_key="AIzaSyA2_Sl2UeTzx38X861XJ-Ny7VlkWmK_KZo"
youtube= build('youtube','v3',developerKey=api_key)
# print(type(youtube))


def videoids(request):
    req=youtube.search().list(q="DJango Tutorial in Bangla", part="snippet", type="video",maxResults=2)
    res=req.execute()
    id=[]
    for r in res['items']:
        id.append(r['id']['videoId'])
        print(r['id']['videoId'])
    return render(request, 'index.html',{'res':res,'id':id})

# print(res['items'])
def channel(request):
    req=youtube.channels().list(id="UCk2uIBpGABdatWhMgKNT_iA",part="contentDetails").execute()
    playlist_id=req['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    res=youtube.playlistItems().list(playlistId=playlist_id,part='snippet',maxResults=200).execute()
    id=[]
    next_page_token=None
    while 1:
        res=youtube.playlistItems().list(playlistId=playlist_id,part='snippet',maxResults=200,pageToken=next_page_token).execute()
        for r in res['items']:
            id.append(r['snippet']['resourceId']['videoId'])
        next_page_token=res.get('nextPageToken')
        if next_page_token is None:
            break
    print(len(id))
    # print(res['items'][0]['snippet']['resourceId']['videoId'])
    return render(request, 'index.html')

