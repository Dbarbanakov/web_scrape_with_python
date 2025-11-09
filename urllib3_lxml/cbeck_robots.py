import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://news.ycombinator.com/robots.txt")
rp.read()

delay = rp.crawl_delay("*")
print(delay)  # prints 30
