import pytest
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment


def node_summary(node):
    """Helper to identify nodes in assertions."""
    if isinstance(node, Tag):
        return f"<{node.name}>"
    elif isinstance(node, Comment):
        return "<!--comment-->"
    elif isinstance(node, NavigableString):
        # Normalize whitespace for robust comparisons
        return str(node).strip() or "<ws>"
    else:
        return type(node).__name__


def test_iterates_over_all_descendants_simple_tree():
    html = """<html><body><p>Hi <b>there</b></p></body></html>"""
    soup = BeautifulSoup(html, "html.parser")

    nodes = list(soup)
    # Expect depth-first traversal over all descendants (excluding the soup object)
    summaries = [node_summary(n) for n in nodes]

    assert summaries == [
        "<html>",
        "<body>",
        "<p>",
        "Hi",
        "<b>",
        "there",
    ]


def test_iteration_over_multiple_top_level_tags():
    html = "<p>one</p><p>two</p>"
    soup = BeautifulSoup(html, "html.parser")

    summaries = [node_summary(n) for n in soup]
    # Two p tags and their text nodes
    assert summaries == ["<p>", "one", "<p>", "two"]


def test_iteration_includes_strings_and_comments():
    html = "<div>text<!--comment--><span>more</span></div>"
    soup = BeautifulSoup(html, "html.parser")

    summaries = [node_summary(n) for n in soup]
    assert "<div>" in summaries
    assert "text" in summaries
    assert "<!--comment-->" in summaries
    assert "<span>" in summaries
    assert "more" in summaries


def test_empty_document_iterates_to_zero_nodes():
    soup = BeautifulSoup("", "html.parser")
    nodes = list(soup)
    assert nodes == []


def test_multiple_iterations_produce_same_sequence():
    html = "<div><p>a</p><p>b</p></div>"
    soup = BeautifulSoup(html, "html.parser")

    first = [node_summary(n) for n in soup]
    second = [node_summary(n) for n in soup]

    assert first == second
