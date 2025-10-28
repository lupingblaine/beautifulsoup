from bs4 import BeautifulSoup, SoupStrainer
import sys

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    parser = "xml" if filename.endswith(".xml") else "html.parser"
    # only deal with <a>
    only_links = SoupStrainer("a")
    soup = BeautifulSoup(f, parser, parse_only=only_links)

links = soup.find_all("a")
for link in links:
    print(link.get("href"))

print("Task2 done: print all links")


