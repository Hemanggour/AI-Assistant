from googleapiclient.discovery import build
import webbrowser
import APIs

API_KEY = APIs.api('youtube')

def youtube_search(query, max_results=1):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Perform a search
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results,
        type='video'  # Specify the type to filter only video results
    ).execute()

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            video_id = search_result['id']['videoId']
            video_title = search_result['snippet']['title']
            return f"https://www.youtube.com/watch?v={video_id}&autoplay=1"
            # webbrowser.open(f"https://www.youtube.com/watch?v={video_id}&autoplay=1")

if __name__ == "__main__":
#     query = input("Enter the search query: ")
    query: str = None
    youtube_search(query)