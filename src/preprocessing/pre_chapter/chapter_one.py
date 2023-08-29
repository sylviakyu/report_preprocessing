from preprocessing.pre_config import (
    ChapterTemplate, ReportOutputData, ReportProcessingData,
    BalanceColumn, TextSimple, TextType, TitleText, TextBullet,
    EmptyNote, BulletType
)


class ProcessingChapterOne(ChapterTemplate):
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
            TextSimple(text_type=TextType.h1.value,text=TitleText.one.value)
            )

        if process_data:
            self.report_output.report_object.append(BalanceColumn(
                content=[
                    TextBullet(text_type=TextType.p3.value, bullet_type=BulletType.number.value,
                                text=process_data,bullet_indent=16)
                ]
            ))
        else:
            self.report_output.report_object.append(
                TextSimple(text_type=TextType.p3.value,text=EmptyNote.one.value)
            )
