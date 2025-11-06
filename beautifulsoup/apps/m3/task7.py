
import sys
from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer


def make_attrs_xformer():
    def attrs_xformer(tag):
        if tag.name == "p":
            attrs = dict(tag.attrs) if tag.attrs else {}
            attrs["class"] = ["test"]  
            return attrs
        return tag.attrs
    return attrs_xformer

def main():
    if len(sys.argv) < 2:
        print("Usage: python task7.py <input.html|input.xml>")
        return
    filename = sys.argv[1]
    parser = "xml" if filename.lower().endswith(".xml") else "html.parser"
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    replacer = SoupReplacer(attrs_xformer=make_attrs_xformer())
    soup = BeautifulSoup(html, parser, replacer=replacer)

    out = f"p_add_class_test.{filename.split('.')[-1]}"
    with open(out, "w", encoding="utf-8") as fw:
        fw.write(soup.prettify())

    print(f"Task7 done: wrote {out}")

if __name__ == "__main__":
    main()
