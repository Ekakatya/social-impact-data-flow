import requests 
from datetime import datetime, timedelta

NEWS_API_URL = "https://newsapi.org/v2/everything"

def fetch_all_news_data(api_key: str, query: str, days_limit: int, page_size: int) -> list:

    print(f"-> Starting extraction for query: '{query}'...")
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_limit)
    
    params = {
        'q': query,
        'from': start_date.strftime('%Y-%m-%d'),
        'to': end_date.strftime('%Y-%m-%d'),
        'sortBy': 'publishedAt',
        'pageSize': page_size,
        'apiKey': api_key
    }
    
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        
        data = response.json()
        articles = data.get('articles', [])
        
        print(f"-> Successfully extracted {len(articles)} articles.")
        return articles
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error occurred: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
        
    return []