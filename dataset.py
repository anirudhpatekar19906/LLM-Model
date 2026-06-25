"""This script scrapes the text content of the book "Neural Networks and Deep Learning by Michael Nielsen, which is available online for free. 
It collects the text from all chapters and saves it into a single file called "full_book.txt". 
The script uses the 'requests' library to fetch the web pages and `BeautifulSoup` to parse the HTML and extract the text content.
It also includes a delay between requests to avoid overwhelming the server."""
import requests
from bs4 import BeautifulSoup
import time

chapters = [
    "http://neuralnetworksanddeeplearning.com/chap1.html",
    "http://neuralnetworksanddeeplearning.com/chap2.html",
    "http://neuralnetworksanddeeplearning.com/chap3.html",
    "http://neuralnetworksanddeeplearning.com/chap4.html",
    "http://neuralnetworksanddeeplearning.com/chap5.html",
    "http://neuralnetworksanddeeplearning.com/chap6.html",
]

all_text = ""

for i, url in enumerate(chapters, 1):
    print(f"Downloading chapter {i}...")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for tag in soup(["script", "style", "nav", "header", "footer"]):
        tag.decompose()

    text = soup.get_text(separator="\n")
    lines = [line.strip() for line in text.splitlines()]
    clean = "\n".join(line for line in lines if line)

    all_text += f"\n\n=== CHAPTER {i} ===\n\n" + clean
    time.sleep(1)

# Save ALL chapters into ONE single file
with open("full_book.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("✅ Done! Everything saved in one file: full_book.txt")