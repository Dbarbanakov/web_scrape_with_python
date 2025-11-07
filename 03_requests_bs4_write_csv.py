import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png"
response = requests.get(url)
with open("image.jpg", "wb") as file:
    file.write(response.content)


BASE_URL = "https://news.ycombinator.com"
USERNAME = ""
PASSWORD = ""

s = requests.Session()

data = {"goto": "news", "acct": USERNAME, "pw": PASSWORD}
r = s.post(f"{BASE_URL}/login", data=data)

soup = BeautifulSoup(r.text, "html.parser")
if soup.find(id="logout") is not None:
    print("Successfully logged in")
else:
    print("Authentication Error")


r = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(r.text, "html.parser")
links = soup.find_all("tr", class_="athing")

formatted_links = []

for link in links:
    data = {
        "id": link["id"],
        "title": link.find_all("td")[2].a.text,
        "url": link.find_all("td")[2].a["href"],
        "rank": int(link.find_all("td")[0].span.text.replace(".", "")),
    }
    formatted_links.append(data)

for link in formatted_links:
    print(link["title"])

# Define the CSV file path
csv_file = "hacker_news_posts.csv"

# Write data to CSV
with open(csv_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["id", "title", "url", "rank"])
    writer.writeheader()
    for row in formatted_links:
        writer.writerow(row)
