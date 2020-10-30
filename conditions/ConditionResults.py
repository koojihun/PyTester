class ConditionsResult:

    def __init__(self):
        self.target_stock = None
        self.from_date = None
        self.to_date = None
        self.volume_days = None
        self.volume_percents = None
        self.buy_conditions = list()
        self.sell_conditions = list()

    def clear_target_stock(self):
        self.target_stock = None

    def clear_date(self):
        self.from_date = None
        self.to_date = None

    def clear_volume(self):
        self.volume_days = None
        self.volume_percents = None

    def clear_buy_conditions(self):
        self.buy_conditions.clear()

    def clear_sell_conditions(self):
        self.sell_conditions.clear()
