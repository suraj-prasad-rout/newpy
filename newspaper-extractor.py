import requests
from bs4 import BeautifulSoup

url = 'https://sambadepaper.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all img tags in the HTML
img_tags = soup.find_all('img')

# Extract the src attribute from each img tag
image_urls = [img['src'] for img in img_tags]

# Print the image URLs
for img_url in image_urls:
    print(img_url)
