from preprocessing.pre_config import (
    ChapterTemplate, ReportOutputData, ReportProcessingData,
    BalanceColumn, TextSimple, TextType, TitleText, TextBullet,
    PrePageBreak, PreSpacer
)


class ProcessingChapterTwo(ChapterTemplate):
    def __init__(
            self,
            report_output: ReportOutputData,
            processing: ReportProcessingData
        ) -> None:
        self.report_output = report_output
        self.processing = processing

    def _process_data(self):
        """"""
        process_data = []
        return process_data

    def append_report_object(self):
        process_data = self._process_data()

        # title
        self.report_output.report_object.append(
            TextSimple(text_type=TextType.h1.value,text=TitleText.two.value)
            )

        ## balance column
        col = []

        # about panel
        col.append(TextSimple(text_type=TextType.p3.value, text="test"))
        col.append(PreSpacer())
        # liimitationss
        col.append(TextBullet(text_type=TextType.p3.value, text="test"))
        col.append(PreSpacer())
        # ngs
        col.append(TextSimple(text_type=TextType.p3.value, text="test"))
        col.append(PreSpacer())
        # db
        col.append(TextBullet(text_type=TextType.p3.value, text="test"))
        col.append(PreSpacer())
        # disclaimer
        for _data in process_data:
            col.append(TextSimple(text_type=TextType.p3.value, text=_data["text"]))
            col.append(PreSpacer())

        self.report_output.report_object.append(BalanceColumn(content=col))

        # finish
        self.report_output.report_object.append(PrePageBreak())
