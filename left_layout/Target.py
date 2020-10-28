from PyQt5.QtWidgets import QMessageBox

import Market
from Stock import Stock

class Target:

    target_market_list = ["KOSPI 전체", "KOSDAQ 전체", "KOSPI 특정", "KOSDAQ 특정"]
    err_msg = "결과가 존재하지 않습니다."

    def __init__(self, main_window):
        self.main_window = main_window
        self.target_market_combo_box = main_window.target_market_combo_box
        self.target_search_condition_combo_box = main_window.target_search_condition_combo_box
        self.target_search_line_edit = main_window.target_search_line_edit
        self.target_search_btn = main_window.target_search_btn
        self.target_search_result_line_edit = main_window.target_search_result_line_edit
        self.target_ok_btn = main_window.target_ok_btn

        self.target_market_combo_box.currentIndexChanged.connect(self._handle_chage_market)
        self._handle_chage_market()

        self.target_search_btn.clicked.connect(self._handle_search)
        self.target_ok_btn.clicked.connect(self._handle_ok)

        self.found = None

    def _handle_chage_market(self):
        idx = self.target_market_combo_box.currentIndex()
        if idx == 0 or idx == 1:
            self._switch_search_function(False)
        else:
            self._switch_search_function(True)

    def _switch_search_function(self, bool):
        self.target_search_condition_combo_box.setEnabled(bool)
        self.target_search_line_edit.clear()
        self.target_search_line_edit.setEnabled(bool)
        self.target_search_btn.setEnabled(bool)
        self.target_search_result_line_edit.clear()
        self.target_search_result_line_edit.setEnabled(bool)
        self.found = None

    def _handle_search(self):

        self.found = None

        target_market = self.target_market_combo_box.currentText()
        key = self.target_search_line_edit.text()
        search_condition = self.target_search_condition_combo_box.currentText()

        if key == "":
            return

        # 1. KOSPI 선택
        if target_market == Target.target_market_list[2]:
            if search_condition == "종목 코드" and Market.kospi_get_name_by_code(key) is not None:
                self.found = Stock(key, Market.kospi_get_name_by_code(key))
            elif search_condition == "종목 이름" and Market.kospi_get_code_by_name(key) is not None:
                self.found = Stock(Market.kospi_get_code_by_name(key), key)

        # 2. KOSDAQ 선택
        else:
            if search_condition == "종목 코드" and Market.kospi_get_name_by_code(key) is not None:
                self.found = Stock(key, Market.kosdaq_get_name_by_code(key))
            elif search_condition == "종목 이름" and Market.kospi_get_code_by_name(key) is not None:
                self.found = Stock(Market.kosdaq_get_code_by_name(key), key)

        if self.found is None:
            self.target_search_result_line_edit.setText(Target.err_msg)
        else:
            self.target_search_result_line_edit.setText(self.found.code + " " + self.found.name)

    def _handle_ok(self):
        target_market = self.target_market_combo_box.currentText()
        if target_market == Target.target_market_list[0] or target_market == Target.target_market_list[1]:
            self.main_window.target_text_label.setText(target_market)
            self._switch_search_function(False)
        else:
            if self.found is not None:
                self.main_window.target_text_label.setText(self.found.code + "\n" + self.found.name)
                self._switch_search_function(True)