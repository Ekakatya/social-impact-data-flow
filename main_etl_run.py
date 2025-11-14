import pandas as pd
from src.extract import fetch_all_news_data
from src.transform_load import clean_and_analyze_data, load_to_database

API_KEY = "7dc45bf9d5164348a8456170f293aef2"  
QUERY = "consumer spending OR supply chain OR FMCG market"
PAGE_SIZE = 20
LIMIT_DAYS = 3

DB_NAME = 'news_dwh.db'
TABLE_NAME = 'sentiment_articles'


if __name__ == "__main__":
    print("--- Starting Full ETL Pipeline in Container ---")
    
    # E: Extraction
    raw_articles_list = fetch_all_news_data(API_KEY, QUERY, LIMIT_DAYS, PAGE_SIZE)
    raw_df = pd.DataFrame(raw_articles_list)
    
    if raw_df.empty:
        print("Pipeline aborted: No data extracted.")
    else:
        # T: Transformation and Analysis
        transformed_df = clean_and_analyze_data(raw_df)
        
        # L: Loading in DWH
        if not transformed_df.empty:
            load_to_database(transformed_df, DB_NAME, TABLE_NAME)
        else:
            print("Pipeline aborted: Transformation resulted in empty data.")
        
        print("--- Pipeline completed successfully! ---")