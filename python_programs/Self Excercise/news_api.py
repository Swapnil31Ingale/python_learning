# Use the NewsAPI and the requests module to fetch 
# the daily news related to different topics. 
# Go to: https://newsapi.org/ and explore the 
# various options to build you application

import requests

URL = "https://newsapi.org/"
top = "v2/top-headlines?"
everything =  "v2/everything?"
country_list = ["us", "in"]
apiKey = "########################"

print("################Please enter your choice below as asked for################")
country = str(input("Please enter your country either 'us' or 'in': ")).lower()
news = str(input("News type either 'top' or 'everything': ")).lower()

# Build the API endpoint based on user input
endpoint = top if news == 'top' else everything

# Construct the complete URL for the API request
complete_url = f"{URL}{endpoint}country={country}&apiKey={apiKey}"
print(complete_url)

# Make the API request and get the response and its response type
response = requests.get(complete_url)
# print(response)
response_type = response.headers['Content-Type']
# print(response_type)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    # print("#####News data#####")
    news_data = response.json()
    # print(news_data)
    # Display the news articles
    # print("#####News Articles#####")
    articles = news_data.get('articles', [])
    # print(articles)
    for index, article in enumerate(articles, start=1):
        print(f"\nArticle {index}:")
        print(f"Title: {article.get('title', 'N/A')}")
        print(f"Author: {article.get('author', 'N/A')}")
        print(f"Description: {article.get('description', 'N/A')}")
        print(f"URL: {article.get('url', 'N/A')}")
else:
    print(f"Failed to fetch news. Status code: {response.status_code}")


# import requests

# class NewsFetcher:
#     def __init__(self, api_key):
#         self.URL = "https://newsapi.org/"
#         self.top = "v2/top-headlines?"
#         self.everything = "v2/everything"
#         self.api_key = api_key

#     def fetch_news(self, country, news_type):
#         # Build the API endpoint based on user input
#         endpoint = self.top if news_type == 'top' else self.everything

#         # Construct the complete URL for the API request
#         complete_url = f"{self.URL}{endpoint}country={country}&apiKey={self.api_key}"

#         # Make the API request and get the response
#         response = requests.get(complete_url)

#         # Check if the request was successful (status code 200)
#         if response.status_code == 200:
#             # Parse the JSON response
#             news_data = response.json()

#             # Display the news articles
#             articles = news_data.get('articles', [])
#             for index, article in enumerate(articles, start=1):
#                 print(f"\nArticle {index}:")
#                 print(f"Title: {article.get('title', 'N/A')}")
#                 print(f"Author: {article.get('author', 'N/A')}")
#                 print(f"Description: {article.get('description', 'N/A')}")
#                 print(f"URL: {article.get('url', 'N/A')}")
#         else:
#             print(f"Failed to fetch news. Status code: {response.status_code}")

# # Usage
# api_key = "YOUR_API_KEY"  # Replace with your actual NewsAPI key
# news_fetcher = NewsFetcher(api_key)
# country_input = input("Please enter your country either 'us' or 'in': ").lower()
# news_type_input = input("News type either 'top' or 'everything': ").lower()
# news_fetcher.fetch_news(country_input, news_type_input)



# import requests
# import json

# query = input("What type of news are you interested in? ")
# url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=#######"
# r = requests.get(url)
# news = json.loads(r.text)
# # print(news, type(news))
# for article in news["articles"]:
#   print(article["title"])
#   print(article["description"])
#   print("--------------------------------------")

