import requests
import APIs

GOOGLE_API_KEY = APIs.api('customSearch')
GOOGLE_CSE_ID = APIs.api('CSE_ID')

def google_search(query, num_results=1):
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_CSE_ID}&q={query}&num={num_results}"
    response = requests.get(url)
    results = response.json().get('items', [])

    search_results = []
    for result in results:
        title = result.get('title')
        link = result.get('link')
        snippet = result.get('snippet')
        search_results.append({
            'title': title,
            'link': link,
            'snippet': snippet
        })
    
    return search_results

if __name__ == "__main__":
    # Take custom input from the user
    query = input("Enter the search query: ")
    
    # Perform Google search
    results = google_search(query)
    
    # Print the results
    print("Google Search Results:")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Snippet: {result['snippet']}")
        print()
