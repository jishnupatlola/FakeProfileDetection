import pandas as pd
import re

def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\w+', '', text)     
    text = re.sub(r'#\w+', '', text)     
    text = re.sub(r'\W', ' ', text)      
    text = text.lower()                  
    return text

def preprocess_data(data):
    data['cleaned_tweets'] = data['tweets'].apply(lambda x: [clean_text(tweet) for tweet in x])
    return data

if __name__ == "__main__":
    raw_data = {'username': 'someuser', 'tweets': ['Check out http://example.com #example', 'Hello @world!']}
    df = pd.DataFrame([raw_data])
    preprocessed_data = preprocess_data(df)
    print(preprocessed_data)
