import pandas as pd 
import sqlite3
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def clean_and_analyze_data(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()
    
    initial_count = len(df)

    df.dropna(subset=['title', 'publishedAt', 'url'], inplace=True) 
    
    if len(df) != initial_count:
        print(f"   - Removed {initial_count - len(df)} rows with missing critical data.")
        
    try:
        df['publishedAt'] = pd.to_datetime(df['publishedAt'], utc=True) 
    except Exception as e:
        print(f"   - Error converting date: {e}")
        return pd.DataFrame()
    
    sid = SentimentIntensityAnalyzer()
    
    df['sentiment_score'] = df['title'].apply(lambda title: sid.polarity_scores(title)['compound'])
    

    transformed_df = df[['publishedAt', 'title', 'source', 'url', 'sentiment_score']].copy()
    
    transformed_df['source_name'] = transformed_df['source'].apply(
        lambda x: x.get('name', 'N/A') if isinstance(x, dict) else 'N/A'
    )
    
    final_columns = ['publishedAt', 'title', 'source_name', 'url', 'sentiment_score']
    
    return transformed_df[final_columns]


def load_to_database(df: pd.DataFrame, db_name: str, table_name: str):

    conn = None
    try:

        conn = sqlite3.connect(db_name)

        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        count = pd.read_sql(f"SELECT COUNT(*) FROM {table_name}", conn).iloc[0, 0]
        print(f"-> Successfully loaded {count} records into table '{table_name}'.")
        
    except Exception as e:
        print(f"!!! CRITICAL ERROR during database load: {e}")
        
    finally:
        if conn:
            conn.close()