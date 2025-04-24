import requests

query = input("News you want to see : ")
api = "e798431e2da34746925caf9ca320cda2"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-03-24sortBy=publishedAt&apiKey={api}"

print(url)

c = requests.get(url)

news_data = c.json()
articles = news_data["articles"]

for index, article in enumerate(articles):
    print(index+1 ,article["title"])
    print(article["description"])
    print(article["url"])
    print("\n-------------------------------------------------\n")