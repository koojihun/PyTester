from conditions.Target import Target


class ConditionManager:

    target_stock = None
    date = None
    volume = None
    buy_condition = None
    sell_condition = None


    def __init__(self, main_window, markets):

        self.main_window = main_window
        self.markets = markets

        self.target = Target(main_window, self, markets)

        self._set_ui()

    def _set_ui(self):
        self.main_window.target_clear_btn.clicked.connect(self._clear_target_stock)
        self.main_window.date_clear_btn.clicked.connect(self._clear_date)
        self.main_window.volume_label_clear_btn.clicked.connect(self._clear_volume)
        self.main_window.buy_condition_clear_btn.clicked.connect(self._clear_buy_condition)
        self.main_window.sell_condition_clear_btn.clicked.connect(self._clear_sell_condition)

    def _clear_target_stock(self):
        ConditionManager.target_stock = None
        self.main_window.target_text_label.setText("")

    def _clear_date(self):
        ConditionManager.date = None
        self.main_window.date_text_label.setText("")

    def _clear_volume(self):
        ConditionManager.volume = None
        self.main_window.volume_text_label.setText("")

    def _clear_buy_condition(self):
        ConditionManager.buy_condition = None
        self.main_window.buy_condition_text_label.setText("")

    def _clear_sell_condition(self):
        ConditionManager.sell_condition = None
        self.main_window.sell_condition_text_label.setText("")
