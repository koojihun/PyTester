from Utils.Dialog import Dialog
from Utils.Finals import *


class SellConditions:

    def __init__(self, main_window, condition_manager):
        self.main_window = main_window
        self.condition_manager = condition_manager
        self.condition_combo_box_a = main_window.sell_condition_combo_box_A
        self.condition_combo_box_b = main_window.sell_condition_combo_box_B

        self.sell_condition_ok_btn = main_window.sell_condition_ok_btn
        self.sell_condition_ok_btn.clicked.connect(self._handle_ok_btn)

    def _handle_ok_btn(self):

        a_idx = self.condition_combo_box_a.currentIndex()
        b_idx = self.condition_combo_box_b.currentIndex()

        if a_idx == b_idx:
            Dialog.show_err("같은 조건을 비교할 수 없습니다.")
            return
        else:
            if (a_idx, b_idx) in self.condition_manager.results.sell_conditions:
                Dialog.show_err("이미 존재하는 매도 조건입니다.")
                return

            if len(self.condition_manager.results.sell_conditions) >= 3:
                Dialog.show_err("매수 조건은 3개까지 입력 가능합니다.")
                return

            self.condition_manager.results.sell_conditions.append((a_idx, b_idx))
            already_str = self.main_window.sell_condition_text_label.text()
            if already_str != "":
                already_str += "\n"
            self.main_window.sell_condition_text_label.setText(
                already_str
                + CONDITIONS_NAMES[a_idx]
                + " < "
                + CONDITIONS_NAMES[b_idx]
            )
