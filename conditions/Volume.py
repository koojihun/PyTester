
class Volume:

    def __init__(self, main_window, condition_manager):

        self.main_window = main_window
        self.condition_manager = condition_manager

        self.volume_days_spinBox = main_window.volume_days_spinBox
        self.volume_percents_spinBox = main_window.volume_percents_spinBox

        main_window.volume_ok_btn.clicked.connect(self._handle_ok_btn)

    def _handle_ok_btn(self):

        days = self.volume_days_spinBox.value()
        percents = self.volume_percents_spinBox.value()

        self.condition_manager.results.volume_days = days
        self.condition_manager.results.volume_percents = percents

        self.volume_days_spinBox.setValue(-1)
        self.volume_percents_spinBox.setValue(-1)

        self.main_window.volume_text_label.setText("이전 " + str(days) + "일 평균\n" + str(percents) + "% 증가 조건")
