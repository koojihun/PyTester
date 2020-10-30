from Finals import *
from Stock import Stock


class Target:

    def __init__(self, main_window, condition_manager, markets):
        self.main_window = main_window
        self.condition_manager = condition_manager
        self.markets = markets.markets
        self.target_market_combo_box = main_window.target_market_combo_box
        self.target_search_condition_combo_box = main_window.target_search_condition_combo_box
        self.target_search_line_edit = main_window.target_search_line_edit
        self.target_search_btn = main_window.target_search_btn
        self.target_search_result_line_edit = main_window.target_search_result_line_edit
        self.target_ok_btn = main_window.target_ok_btn

        self.target_market_combo_box.currentIndexChanged.connect(self._handle_change_market)
        self._handle_change_market()

        self.target_search_btn.clicked.connect(self._handle_search)
        self.target_ok_btn.clicked.connect(self._handle_ok)

        self.found = None

    def _handle_change_market(self):

        idx = self.target_market_combo_box.currentIndex()
        if idx == KOSPI_SELECT_ONE or idx == KOSDAQ_SELECT_ONE:
            self._switch_search_function(True)
        else:
            self._switch_search_function(False)

    def _switch_search_function(self, flag):

        self.target_search_condition_combo_box.setEnabled(flag)
        self.target_search_line_edit.setEnabled(flag)
        self.target_search_btn.setEnabled(flag)
        self.target_search_result_line_edit.setEnabled(flag)

        self.target_search_line_edit.clear()
        self.target_search_result_line_edit.clear()

        self.found = None

    def _handle_search(self):

        target_market_idx = self.target_market_combo_box.currentIndex()
        search_condition_idx = self.target_search_condition_combo_box.currentIndex()
        key = self.target_search_line_edit.text()

        if key == "":
            return

        self.found = None

        # 종목 코드로 검색한 경우.
        if search_condition_idx == SEARCH_CONDITION_CODE \
                and self.markets[target_market_idx].get_name(key) is not None:
            self.found = Stock(target_market_idx, key, self.markets[target_market_idx].get_name(key))

        # 종목 이름으로 검색한 경우.
        elif search_condition_idx == SEARCH_CONDITION_NAME \
                and self.markets[target_market_idx].get_code(key) is not None:
            self.found = Stock(target_market_idx, self.markets[target_market_idx].get_code(key), key)

        if self.found is None:
            self.target_search_result_line_edit.setText(NOT_EXIST_MESSAGE)
        else:
            self.target_search_result_line_edit.setText(self.found.code + " " + self.found.name)

    def _handle_ok(self):
        target_market_idx = self.target_market_combo_box.currentIndex()
        if target_market_idx == KOSPI_SELECT_ALL or target_market_idx == KOSDAQ_SELECT_ALL:
            self.main_window.target_text_label.setText(self.target_market_combo_box.currentText())
            self.condition_manager.target_stock = Stock(target_market_idx, "", "")
            self._switch_search_function(False)
        else:
            if self.found is not None:
                self.main_window.target_text_label.setText(MARKET_NAMES[target_market_idx] + "\n"
                                                           + self.found.code + "\n"
                                                           + self.found.name)
                self.condition_manager.target_stock = self.found
                self._switch_search_function(True)
