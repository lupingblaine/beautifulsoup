from bs4 import BeautifulSoup, SoupStrainer
import sys

filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as f:
    parser = "xml" if filename.endswith(".xml") else "html.parser"
    # deal with all tags, but only store tag
    all_tags_strainer = SoupStrainer(lambda tag: True)  # 保留所有标签
    soup = BeautifulSoup(f, parser, parse_only=all_tags_strainer)

all_tags = set(tag.name for tag in soup.find_all())
print(all_tags)

print("Task3 done: all tags printed")

