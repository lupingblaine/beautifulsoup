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



## Part3 
Changed：
# __init__.py in bs4:
1.
from .soupreplacer import SoupReplacer
2.
def __init__(
    self,
    markup: _IncomingMarkup = "",
    features: Optional[Union[str, Sequence[str]]] = None,
    builder: Optional[Union[TreeBuilder, Type[TreeBuilder]]] = None,
    parse_only: Optional[SoupStrainer] = None,
    replacer: Optional[SoupReplacer] = None,   # ✅ add
    from_encoding: Optional[_Encoding] = None,
    exclude_encodings: Optional[_Encodings] = None,
    element_classes: Optional[Dict[Type[PageElement], Type[PageElement]]] = None,
    **kwargs: Any,
):
3.
self.replacer = replacer


 # _htmlparser.py in bs4/builder:

def handle_starttag(self, name, attrs):
    if self.soup and getattr(self.soup, "replacer", None):
        name = self.soup.replacer.replace(name)
    super().handle_starttag(name, attrs)

def handle_endtag(self, name):
    if self.soup and getattr(self.soup, "replacer", None):
        name = self.soup.replacer.replace(name)
    super().handle_endtag(name)


Create:
soupreplacer.py


# How to Run Task6:
go into the file location:
```bash
cd beautifulsoup
cd apps
cd m2
```
Run test
```bash
python task6.py test_case.html
```

# Test of API：
In bs4/test:
test_soupreplacer.py can test the api of soupreplacer

```bash
pip install pytest
```
```bash
cd ..
```
until go to the beautifulsoup 

```bash
cd ..
```

```bash
pytest bs4/test/test_soupreplacer.py -v
```
The result I got:
env) luping@lupingdeAir beautifulsoup % pytest bs4/test/test_soupreplacer.py -v

====================================================================== test session starts =======================================================================
platform darwin -- Python 3.11.6, pytest-8.4.2, pluggy-1.6.0 -- /Users/luping/Desktop/beautifulsoup/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/luping/computer science/UCI/262P/project/beautifulsoup
configfile: pyproject.toml
collected 3 items                                                                                                                                                

bs4/test/test_soupreplacer.py::test_single_replacement PASSED                                                                                              [ 33%]
bs4/test/test_soupreplacer.py::test_multiple_replacements PASSED                                                                                           [ 66%]
bs4/test/test_soupreplacer.py::test_other_tags_unchanged PASSED                                                                                            [100%]

======================================================================= 3 passed in 0.04s ========================================================================
(.venv) luping@lupingdeAir beautifulsoup % 

