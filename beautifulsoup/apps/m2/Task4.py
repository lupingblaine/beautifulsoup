from bs4 import BeautifulSoup, SoupStrainer
import sys

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    parser = "xml" if filename.endswith(".xml") else "html.parser"
    # only deal with id
    id_strainer = SoupStrainer(attrs={"id": True})
    soup = BeautifulSoup(f, parser, parse_only=id_strainer)

tags_with_id = soup.find_all(attrs={"id": True})
for tag in tags_with_id:
    print(tag)

print("Task4 done: tags with id")

