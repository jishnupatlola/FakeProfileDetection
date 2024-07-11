
import requests
from bs4 import BeautifulSoup

def collect_twitter_data(username):
    url = f'https://twitter.com/{username}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract relevant data
    profile_data = {
        'username': username,
        'tweets': [tweet.text for tweet in soup.find_all('div', {'class': 'tweet'})]
    }
    
    return profile_data

if __name__ == "__main__":
    username = 'someuser'
    data = collect_twitter_data(username)
    print(data)
