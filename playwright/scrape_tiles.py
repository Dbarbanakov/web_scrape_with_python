from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import logging

# Set up logging to troubleshoot if anything goes wrong
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

with sync_playwright() as p:
    logging.info("Starting The Browser")
    browser = p.firefox.launch()  # headless by dfrom playwright.sync_api import sync_playwrightefault

    # Load the Hacker News homepage
    logging.info("Loading Hacker News homepage")
    page = browser.new_page()
    page.goto("https://news.ycombinator.com/")

    # Get page source and parse it with BeautifulSoup
    logging.info("Parsing page source with BeautifulSoup")
    soup = BeautifulSoup(page.content(), "html.parser")

    # Find all titles on the page (class - titleline)
    logging.info("Finding all story titles on the page")
    titles = soup.find_all("span", class_="titleline")

    if titles:
        logging.info(f"Found {len(titles)} titles. Printing titles:")
        # Print each title
        for title in titles:
            title_link = title.find("a")
            if title_link:
                print(title_link.text)
    else:
        logging.warning("No titles found on the page.")

    # Close the browser
    logging.info("Closing the Browser")
    browser.close()
