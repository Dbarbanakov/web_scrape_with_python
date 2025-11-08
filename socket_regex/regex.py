import re

html_content = '<p>Price : 19.99$</p>'
pattern = r'Price\s*:\s*(\d+\.\d{2})\$'

match = re.search(pattern, html_content)
if match:
    print(match.group(1))  # Output: 19.99