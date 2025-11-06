
import pytest
from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

def test_m3_name_xformer_lambda():
    html = "<div><b>x</b></div>"
    replacer = SoupReplacer(name_xformer=lambda tag: "blockquote" if tag.name=="b" else tag.name)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.find("b") is None
    assert soup.find("blockquote").text == "x"

def test_m3_attrs_xformer_sets_class_on_p():
    html = "<div><p id='x'>text</p></div>"
    def ax(tag):
        if tag.name=="p":
            return {"id": tag.get("id"), "class": ["test"]}
        return tag.attrs
    soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer(attrs_xformer=ax))
    p = soup.find("p")
    assert p is not None
    assert p.get("class")==["test"]

def test_m3_xformer_remove_class():
    html = "<div><span class='a b'>z</span></div>"
    def xf(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]
    soup = BeautifulSoup(html, "html.parser", replacer=SoupReplacer(xformer=xf))
    span = soup.find("span")
    assert "class" not in span.attrs

def test_m3_combined_order_name_then_attrs_then_x():
    html = "<b class='c'>y</b>"
    def ax(tag):
        # after name change, still ok
        if tag.name=="blockquote":
            d = dict(tag.attrs)
            d["data-x"] = "1"
            return d
        return tag.attrs
    log = []
    def xf(tag):
        log.append(tag.name)
    rep = SoupReplacer(name_xformer=lambda t: "blockquote" if t.name=="b" else t.name,
                       attrs_xformer=ax, xformer=xf)
    soup = BeautifulSoup(html, "html.parser", replacer=rep)
    blk = soup.find("blockquote")
    assert blk is not None and blk.get("data-x")=="1"
    assert log and log[0]=="blockquote"

def test_m3_no_crash_on_bad_transformers():
    html = "<p>t</p>"
    rep = SoupReplacer(name_xformer=lambda t: 123, attrs_xformer=lambda t: "oops",
                       xformer=lambda t: (_ for _ in ()).throw(Exception("boom")))
    soup = BeautifulSoup(html, "html.parser", replacer=rep)
    # should parse ok; attrs_xformer invalid ignored
    assert soup.find("p") is not None

def test_m3_rename_affects_end_tag():
    html = "<b>q</b>"
    rep = SoupReplacer(name_xformer=lambda t: "blockquote" if t.name=="b" else t.name)
    soup = BeautifulSoup(html, "html.parser", replacer=rep)
    assert str(soup).startswith("<blockquote>")
    assert str(soup).endswith("</blockquote>")
