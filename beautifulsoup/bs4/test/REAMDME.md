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
