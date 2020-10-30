from conditions.BuyConditions import BuyConditions
from conditions.ConditionResults import ConditionsResult
from conditions.SellConditions import SellConditions
from conditions.Target import Target
from conditions.DateRange import DateRange
from conditions.Volume import Volume


class ConditionManager:

    def __init__(self, main_window, markets):

        self.main_window = main_window
        self.markets = markets

        self.target = Target(main_window, self, markets)
        self.date_range = DateRange(main_window, self)
        self.volume = Volume(main_window, self)
        self.buy_condition = BuyConditions(main_window, self)
        self.sell_condition = SellConditions(main_window, self)

        self.results = ConditionsResult()

        self._set_ui()

    def _set_ui(self):
        self.main_window.target_clear_btn.clicked.connect(self._clear_target_stock)
        self.main_window.date_clear_btn.clicked.connect(self._clear_date)
        self.main_window.volume_clear_btn.clicked.connect(self._clear_volume)
        self.main_window.buy_condition_clear_btn.clicked.connect(self._clear_buy_conditions)
        self.main_window.sell_condition_clear_btn.clicked.connect(self._clear_sell_condition)

    def _clear_target_stock(self):
        self.results.clear_target_stock()
        self.main_window.target_text_label.setText("")

    def _clear_date(self):
        self.results.clear_date()
        self.main_window.date_text_label.setText("")

    def _clear_volume(self):
        self.results.clear_volume()
        self.main_window.volume_text_label.setText("")

    def _clear_buy_conditions(self):
        self.results.clear_buy_conditions()
        self.main_window.buy_condition_text_label.setText("")

    def _clear_sell_condition(self):
        self.results.clear_sell_conditions()
        self.main_window.sell_condition_text_label.setText("")
