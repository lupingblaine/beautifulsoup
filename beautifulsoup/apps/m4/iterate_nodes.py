"""Example application for Milestone 4.

Usage:
    python iterate_nodes.py path/to/file.html
This will parse the file with BeautifulSoup and iterate over all nodes
in the parse tree, printing a short summary for each node.
"""

import sys
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment


def summarize(node) -> str:
    if isinstance(node, Tag):
        return f"TAG   <{node.name}>"
    if isinstance(node, Comment):
        return "COMM  <!--" + str(node).strip() + "-->"
    if isinstance(node, NavigableString):
        text = " ".join(str(node).split())
        return f"TEXT  {text!r}"
    return f"NODE  {type(node).__name__}"


def main(argv=None):
    argv = argv or sys.argv[1:]
    if not argv:
        print("Usage: python iterate_nodes.py path/to/file.html")
        raise SystemExit(1)

    path = Path(argv[0])
    html = path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    for node in soup:
        print(summarize(node))


if __name__ == "__main__":
    main()

