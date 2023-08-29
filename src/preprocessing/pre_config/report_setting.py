from enum import Enum


## Chapter setting
class ChapterList(Enum):
    one = "one"
    two = "two"
    appendix = "appendix"

class EmptyNote(Enum):
    one = "one"
    two = "two"
    appendix = "Not Applicable."


## text
class TitleText(Enum):
    # h1
    one = "Chapter One"
    two = "Chapter Two"
    appendix = "APPENDIX"
