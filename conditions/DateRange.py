from datetime import datetime, timedelta
from Utils.Dialog import Dialog


class DateRange:

    def __init__(self, main_window, condition_manager):
        self.main_window = main_window
        self.condition_manager = condition_manager

        self.from_date_edit = main_window.from_date_edit
        self.to_date_edit = main_window.to_date_edit

        self.yesterday = datetime.today() - timedelta(1)

        self.from_date_edit.setMaximumDate(self.yesterday)
        self.to_date_edit.setMaximumDate(self.yesterday)

        self._init_to_yesterday()

        main_window.date_ok_btn.clicked.connect(self._handle_ok_btn)

    def _init_to_yesterday(self):
        self.from_date_edit.setDateTime(self.yesterday)
        self.to_date_edit.setDateTime(self.yesterday)

    def _handle_ok_btn(self):

        from_date = self.from_date_edit.date()
        to_date = self.to_date_edit.date()

        if from_date > to_date:
            Dialog.show_err("시작일은 종료일보다 작거나 같아야합니다.")
            return

        self.condition_manager.results.from_date = from_date
        self.condition_manager.results.to_date = to_date

        self.main_window.date_text_label.setText("시작일 : " + from_date.toString('yyyy-MM-dd')
                                                 + "\n"
                                                 + "종료일 : " + to_date.toString('yyyy-MM-dd')
                                                 )
        self._init_to_yesterday()

