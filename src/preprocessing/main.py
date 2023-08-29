from preprocessing.pre_config import ChapterList, ReportOutputData, ReportProcessingData
from preprocessing.pre_chapter import (
    ProcessingChapterOne, ProcessingChapterTwo, ProcessingAppendix
)
from .input_data_processing import PreProcessingInputData


class ReportGenerator:
    Chapter = {
        ChapterList.one: ProcessingChapterOne,
        ChapterList.two: ProcessingChapterTwo,
        ChapterList.appendix: ProcessingAppendix,
    }

    def __init__(self, report_output, processing_data):
        self.report_output = report_output
        self.processing = processing_data
        self._chapter = None

    def set_chapter_get_report_object(self, chapter_item: ChapterList):
        if self.Chapter.get(chapter_item):
            self._chapter = self.Chapter.get(chapter_item)(
                self.report_output,
                self.processing
            )
            self._chapter.append_report_object()


def get_preprocessing_output(raw: dict, mnt: str, chapter_list: list) -> ReportOutputData:
    # create output object/ processing object
    report_output = ReportOutputData()

    # set processing data object
    processing = ReportProcessingData(mnt=mnt, raw=raw)

    # pre processing raw data
    PreProcessingInputData(report_output, processing).process()

    # get chapter data by chapter
    generator = ReportGenerator(report_output, processing)
    for _chapter in chapter_list:
        generator.set_chapter_get_report_object(_chapter)
    return report_output, processing
