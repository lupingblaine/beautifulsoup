import sys
from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

def main():
    if len(sys.argv) < 2:
        print("Usage: python task6.py <filename.html|filename.xml>")
        return

    filename = sys.argv[1]


    parser = "xml" if filename.lower().endswith(".xml") else "html.parser"

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(content, parser, replacer=replacer)


    out_file = f"b_to_blockquote.{filename.split('.')[-1]}"

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"✅ Task6 done: {out_file}")

if __name__ == "__main__":
    main()

