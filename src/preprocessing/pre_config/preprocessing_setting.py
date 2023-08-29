from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict


class ChapterTemplate(ABC):
    @abstractmethod
    def _process_data(self):
        pass

    @abstractmethod
    def append_report_object(self):
        pass

@dataclass
class ReportOutputData:
    report_object: list = field(default_factory=list)
    header: dict = field(default_factory=dict)
    doc_title: str = ""
    file_path: str = ""
    folder_path: str = ""

    def dict(self):
        return {k: v for k, v in asdict(self).items()}

@dataclass
class ReportProcessingData:
    mnt: str = ""
    raw: dict = field(default_factory=dict)


# exception
class ProcessingException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
