import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.bbc.com/news"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

data = []

for news in soup.find_all("h2"):
    headline = news.get_text(strip=True)

    if headline:
        data.append([headline, "Not available", "News"])
with open("news.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Headline", "Date", "Category"])
    writer.writerows(data)

print("News headlines saved successfully!")
print("Total headlines:", len(data))