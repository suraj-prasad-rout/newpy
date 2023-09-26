import requests
from bs4 import BeautifulSoup

url = 'https://www.aajtak.in/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Define a list of keywords you want to search for
keywords = ["government", "official", "administration", "authority", "central goverment","ruling party","bjp","congress"]  # Add more keywords as needed

# Find all heading (h1, h2, h3, etc.) and paragraph (p) elements
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
paragraphs = soup.find_all('p')

# Initialize empty lists to store matching headings and paragraphs
matching_headings = []
matching_paragraphs = []

# Function to check if a text contains any of the keywords
def contains_keyword(text):
    text_lower = text.lower()
    for keyword in keywords:
        if keyword in text_lower:
            return True
    return False

# Iterate through the headings and filter those containing keywords
for heading in headings:
    if contains_keyword(heading.get_text()):
        matching_headings.append(heading.get_text())

# Iterate through the paragraphs and filter those containing keywords
for paragraph in paragraphs:
    if contains_keyword(paragraph.get_text()):
        matching_paragraphs.append(paragraph.get_text())

# Print the matching headings
print("Matching Headings:")
for heading in matching_headings:
    print(heading.strip())

# Print the matching paragraphs
print("\nMatching Paragraphs:")
for paragraph in matching_paragraphs:
    print(paragraph.strip())
