
# Milestone 4 – Iterable BeautifulSoup (Summary)

## Code Modification

Add the following method to the `BeautifulSoup` class inside `bs4/__init__.py`,  
right **after the end of `__init__`** and before `copy_self()`:

```python
def __iter__(self):
    """Depth‑first iteration over all nodes in the document tree."""

    def traverse(nodes):
        for node in nodes:
            yield node
            from bs4.element import Tag
            if isinstance(node, Tag):
                for child in traverse(node.contents):
                    yield child

    return traverse(self.contents)
```

---

## How to Run Unit Tests

Inside the project root:

```bash
python -m pytest bs4/tests/test_iterable_soup.py
```

Expected output:

```
5 passed in X.XXs
```

---

## How to Run the Example Application

```bash
python apps/m4/iterate_nodes.py path/to/file.html
```

This prints every node using the new iterable API.

---

## Files Added or Modified

- **Modified**: `bs4/__init__.py`  
  - Inserted the new `__iter__()` implementation.

- **Added**: `bs4/tests/test_iterable_soup.py`  
  - Contains 5 tests validating DFS traversal, node types, and repeatability.

- **Added**: `apps/m4/iterate_nodes.py`  
  - Demo script that iterates and prints all nodes.

