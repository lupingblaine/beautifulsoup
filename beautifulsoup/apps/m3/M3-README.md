# Milestone 3

## Part1 Overview

In this milestone, **SoupReplacer** was extended to support *functional transformation APIs* that modify tags **during parsing**.
New optional parameters were added to allow name, attribute, and side-effect transformations.

### Updated Files

| File                              | Changes                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **bs4/soupreplacer.py**           | Added new parameters `name_xformer`, `attrs_xformer`, and `xformer`.<br>Implemented a new `apply(tag)` function that performs transformations in order: name → attrs → xformer. |
| **bs4/builder/_htmlparser.py**    | After each Tag creation, added a call to `self.soup.replacer.apply(tag)` so transformations happen while parsing.                                                               |
| **apps/m3/task7.py**              | New app script using `attrs_xformer` to add or replace `class=\"test\"` for all `<p>` tags.                                                                                     |
| **bs4/tests/test_replacer_m3.py** | Added 6 test cases for functional interface verification.                                                                                                                       |

---

## Part2 How to Run Task7

### Step 1: Go to project root

```bash
cd beautifulsoup
```

### Step 2: Run the script

If your test file is `apps/m3/sample.html`, use:

```bash
PYTHONPATH=$(pwd) python apps/m3/task7.py apps/m3/sample.html
```

It will create an output file:

```
p_add_class_test.html
```

which adds `class="test"` to all `<p>` tags.

---

## Part3 How to Run Tests


```bash
pip install pytest
PYTHONPATH=$(pwd) pytest bs4/tests/test_replacer_m3.py -v
```
---

