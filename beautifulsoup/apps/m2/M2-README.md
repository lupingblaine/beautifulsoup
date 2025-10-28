# Milestone 2

## Part1 

Notes:
1. HTML files use the built-in parser (html.parser).
2. XML files use lxml-xml, so lxml must be installed.
3. Scripts read the entire file into memory, so very large files may take time.

How to Run Tasks:
go into the file location:
```bash
cd beautifulsoup
cd apps
cd m2
```
Run test
```bash
python task2.py ~(path)/test_case.html
python task3.py ~(path)/test_case.html
python task4.py ~(path)/test_case.html
```

## Part2 BeautifulSoup API Function Locations 

| API | File | Line |
|-----|------|------|
| BeautifulSoup | bs4/__init__.py | 133 |
| SoupStrainer | bs4/filter.py | 313 |
| find_all | bs4/element.py | 2715 |
| find_parent | bs4/element.py | 992 |
| prettify | bs4/element.py | 2601 |
| get | bs4/element.py | 2160 |
| __setitem__ | bs4/element.py | 2223 |

