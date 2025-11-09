from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch()  # headless by default
    context = browser.new_context(viewport={"width": 1920, "height": 1200})
    page = context.new_page()
    page.goto("https://news.ycombinator.com/")
    page.screenshot(path="example-playwright.png")
    browser.close()
