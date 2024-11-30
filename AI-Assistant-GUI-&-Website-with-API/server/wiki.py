import wikipedia
import warnings

# Suppress the BeautifulSoup warning
warnings.filterwarnings("ignore", category=UserWarning, module='wikipedia')

def wikipedia_search(query, num_results=1):
    try:
        # Search Wikipedia for the query
        search_results = wikipedia.search(query, results=num_results)
        
        # Retrieve summaries for each result
        summaries = []
        for title in search_results:
            try:
                summary = wikipedia.summary(title)
                summaries.append({'title': title, 'summary': summary})
            except wikipedia.exceptions.DisambiguationError as e:
                # Handle disambiguation error by skipping ambiguous titles
                print(f"Disambiguation error for {title}: {e}")
            except wikipedia.exceptions.PageError as e:
                # Handle page error by skipping missing titles
                print(f"Page error for {title}: {e}")
        
        return summaries
    
    except wikipedia.exceptions.WikipediaException as e:
        print(f"Wikipedia error: {e}")
        return []

if __name__ == "__main__":
    # Take custom input from the user
    query = input("Enter the search query: ")
    
    # Perform Wikipedia search
    results = wikipedia_search(query)
    
    # Print the results
    if results:
        print("Wikipedia Search Results:")
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Summary: {result['summary']}")
            print()
    else:
        print("No results found or an error occurred.")
