import psycopg2
import requests
from bs4 import BeautifulSoup

# Establish database connection
con = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    user="postgres",
    password="password123",
    database="scrape_demo",
)

# Get a database cursor
cur = con.cursor()

r = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("tr", class_="athing")

for link in links:
    cur.execute(
        """
        INSERT INTO hn_links (id, title, url, rank)
        VALUES (%s, %s, %s, %s)
        """,
        (
            link["id"],
            link.find_all("td")[2].a.text,
            link.find_all("td")[2].a["href"],
            int(link.find_all("td")[0].span.text.replace(".", "")),
        ),
    )

# Commit the data
con.commit()

# Close our database connections
cur.close()
con.close()
