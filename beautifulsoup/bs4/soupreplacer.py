
from typing import Callable, Optional, Dict

class SoupReplacer:

    def __init__(
        self,
        og_tag: Optional[str] = None,
        alt_tag: Optional[str] = None,
        name_xformer: Optional[Callable] = None,
        attrs_xformer: Optional[Callable] = None,
        xformer: Optional[Callable] = None,
    ):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer


    def replace(self, tag_name: str) -> str:
        if self.og_tag is not None and self.alt_tag is not None and tag_name == self.og_tag:
            tag_name = self.alt_tag
        return tag_name


    def apply(self, tag) -> None:
        if self.name_xformer is not None:
            try:
                new_name = self.name_xformer(tag)
                if isinstance(new_name, str) and new_name:
                    tag.name = new_name
            except Exception:
                pass  

        elif self.og_tag is not None and self.alt_tag is not None and tag.name == self.og_tag:
            tag.name = self.alt_tag


        if self.attrs_xformer is not None:
            try:
                new_attrs = self.attrs_xformer(tag)
                if isinstance(new_attrs, dict):
                    tag.attrs = new_attrs
            except Exception:
                pass


        if self.xformer is not None:
            try:
                self.xformer(tag)
            except Exception:
                pass
