import requests

newsApi = "API-KEY"
def getNews(topic):
    print(topic)
    try:
        if topic:
            topicUrl = 'https://newsapi.org/v2/everything'
            params = {
                'q': topic,
                'apiKey': newsApi,
                'language': 'en',
                'sortBy': 'date',   # Optional: sort by relevance or date
                'pageSize': 5   # Number of results
            }
            response = requests.get(topicUrl, params=params)
        else:
            url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsApi}"
            response = requests.get(url)
        if response.status_code == 200:
            news_data = response.json()
            if "articles" in news_data:
                return news_data
        else:
            print(f"Error: {response.status_code}")
            return None
    except KeyError:
        print("Invalid API Key")
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":

    api_key = newsApi
    topic = input("Enter Topic: ")
    articles = getNews(topic)

    if len(articles["articles"]):
        i = 1
        for article in articles['articles']:
            print(f"{i} Source: {article["source"]["name"]}:\n\t{article['title']}")
            i += 1
            # print(f"   Source: {article['source']['name']}")
            # print(f"   URL: {article['url']}\n")
    else:
        print("No articles found or an error occurred.\nCheck Spelling!!")