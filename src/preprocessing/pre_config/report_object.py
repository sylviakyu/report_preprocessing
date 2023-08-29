from dataclasses import dataclass, field, asdict
from enum import Enum, unique


### abstract class
@dataclass
class Report:
    _type: str

    def dict(self):
        return {k: v for k, v in asdict(self).items()}

@dataclass
class ReportObject(Report):
    top_padder: bool = False


### table
@dataclass
class TableObject(ReportObject):
    """abstract table object"""
    _type: str = "table"
    table_type: str = ""
    heading: list = False

@dataclass
class TableList(TableObject):
    _type: str = "table_list"
    content: list = field(default_factory=list)

@dataclass
class TableDict(TableObject):
    _type: str = "table_dict"
    content: dict = field(default_factory=dict)

@dataclass
class TableImage(TableObject):
    _type: str = "table_image"
    content: list = field(default_factory=list)


### text
@dataclass
class TextObject(ReportObject):
    """abstract text object"""
    _type: str = "text"
    text_type: str = ""
    left_indent: int = 12

@dataclass
class TextSimple(TextObject):
    _type: str = "text_simple"
    bullet_type: str = False
    bookmark: str = False
    text: str = ""

@dataclass
class TextBullet(TextObject):
    _type: str = "text_bullet"
    bullet_type: str = "bullet"
    text: list = field(default_factory=list)
    bullet_indent: int = 8


### image
@dataclass
class Image(ReportObject):
    _type: str = "image"
    image_type: str = ""
    image_url: str = ""


### column
@dataclass
class BalanceColumn(ReportObject):
    _type: str = "balance_column"
    column_num: int = 3
    content: list = field(default_factory=list)


### page setting
@dataclass
class PrePageBreak(Report):
    _type: str = "page_break"
    page_break: int = 672

@dataclass
class PreSpacer(Report):
    _type: str = "spacer"
    spacer: int = 12

@dataclass
class Liner(Report):
    _type: str = "liner"
    liner_type: str = "-"


### type
@unique
class TableType(Enum):
    type_a = "type_a"

@unique
class TextType(Enum):
    h1 = "H1"
    h2 = "H2"
    p3 = "P3"
    p4 = "P4"  # note

@unique
class BulletType(Enum):
    bullet = "bullet"
    number = "1"

@unique
class LinerType(Enum):
    dash = "dash"

@unique
class TextTag(Enum):
    line_break = "<br />"
    bold = "<b>"
    bold_close = "</b>"
    sup = "<sup>"
    sup_close = "</sup>"
    under = "<u>"
    under_close = "</u>"
    space = "&nbsp;"*8
