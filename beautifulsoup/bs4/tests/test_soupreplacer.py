import pytest
from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer


def test_single_replacement():
    html = "<html><body><b>Hello</b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    # 确认 <b> 被替换成 <blockquote>
    assert "<b>" not in str(soup)
    assert "<blockquote>" in str(soup)
    assert "</blockquote>" in str(soup)
    assert "Hello" in str(soup)


def test_multiple_replacements():
    html = "<b>One</b><b>Two</b>"
    replacer = SoupReplacer("b", "i")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    result = str(soup)
    # 两个 <b> 都换成了 <i>
    assert result.count("<i>") == 2
    assert result.count("</i>") == 2


def test_other_tags_unchanged():
    html = "<p>Paragraph</p><b>Bold</b>"
    replacer = SoupReplacer("b", "div")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    result = str(soup)
    # <p> 保持不变，<b> 替换成 <div>
    assert "<p>Paragraph</p>" in result
    assert "<b>" not in result
    assert "<div>Bold</div>" in result
