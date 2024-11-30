from newsapi import NewsApiClient
import APIs

newsapi = NewsApiClient(newsApi = APIs.api('news'))

def getNews(topic = ""):
    response = newsapi.get_everything(q= topic,
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

    if response.status_code == 200:
        data = response.json()
        if 'articles' in data:
            return data
        else:
            print("No articles found in the response.")
    elif response.status_code == 401:
        print("Error 401: Unauthorized. Please check your API key.")
    else:
        print(f"Failed to fetch data: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    topic = input("Enter News Topic: ")
    newsData = getNews(topic)
    # for article in newsData['articles']:
    #     print(article['title'])
    print(newsData)