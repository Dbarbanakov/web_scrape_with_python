import asyncio
import aiohttp
from bs4 import BeautifulSoup


# Asynchronous function to fetch the HTML content of the URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


# Asynchronous function to fetch the HTML content of multiple URLs
async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)


# Main function to fetch and parse the HTML content
async def main():
    urls = [
        "https://news.ycombinator.com/news?p=1"
    ] * 25  # Example: same URL for demonstration
    html_pages = await fetch_all(urls)

    all_links = []
    for html in html_pages:
        soup = BeautifulSoup(html, "html.parser")
        links = soup.findAll("tr", class_="athing")
        for link in links:
            data = {
                "id": link["id"],
                "title": link.find_all("td")[2].a.text,
                "url": link.find_all("td")[2].a["href"],
                "rank": int(link.find_all("td")[0].span.text.replace(".", "")),
            }
            all_links.append(data)

    count = 0

    for link in all_links:
        count += 1
        print(
            f"ID: {link['id']}, Title: {link['title']}, URL: {link['url']}, Rank: {link['rank']}"
        )

    print(f"\nnumer of news - {count}")


# Run the main function
asyncio.run(main())
