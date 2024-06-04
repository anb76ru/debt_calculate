from helpers import *
from kivymd.app import MDApp
from debtcalculate import KV
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.snackbar import Snackbar
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window, WindowBase
from kivymd.uix.button import MDFloatingActionButton
from widgets import InfoContent, MemberRow, FlatButton

Window.softinput_mode = 'below_target'


class DebtCalculate(MDApp):
    """Основной класс приложения"""

    title = "Расчет долгов"
    by_who = 'by anb76ru'
    version = "version 0.0.2"
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.part_list_widgets = {}
        self.part_list = {}
        self.info_dialog = None
        self.info_text = "Расчет не производился"

        self.info_dialog = MDDialog(
            title="Как работать с приложением:\n",
            type='custom',
            content_cls=InfoContent(),
            buttons=[
                FlatButton(text="CLOSE", on_release=self.close_info)
            ]
        )

    def on_start(self):
        """Действия при запуске приложения"""

        self.screen.ids.box.add_widget(MDLabel(
            text=self.info_text,
            halign="center",
            font_style='H6'
        ))
    
    def build(self):
        return self.screen

    def get_count_participant(self):
        """Получить количество участников"""

        if self.screen.ids.participant_count.text:
            count = int(self.screen.ids.participant_count.text)
        elif len(self.part_list_widgets):
            count = len(self.part_list_widgets)
        else:
            count = 0
        return count

    def create_table_to_add_data(self):
        """Создать таблицу для заполнения данных"""

        self.screen.ids.table_list.clear_widgets()
        participant_count = self.get_count_participant()
        if participant_count <= 0 or participant_count >= 100:
            return
        for i in range(1, participant_count+1):
            row_color = (0.98, 0.98, 0.98, 1)
            widget = MemberRow(color=row_color, text=str(i))
            self.part_list_widgets[f'user_{i}'] = widget
            self.screen.ids.table_list.add_widget(widget)

    def add_row(self):
        """Добавить строку для ввода данных об участнике и сумме затрат"""

        row_color = (0.98, 0.98, 0.98, 1)
        widget = MemberRow(color=row_color, text=str(len(self.part_list_widgets) + 1))
        self.part_list_widgets[f'user_{len(self.part_list_widgets) + 1}'] = widget
        self.screen.ids.table_list.add_widget(widget)

    def remove_row(self):
        """Удалить строку для ввода данных об участнике и сумме затрат"""

        widget = self.part_list_widgets.pop(f'user_{len(self.part_list_widgets)}')
        self.screen.ids.table_list.remove_widget(widget)

    def fill_part_list(self, widgets_dict: dict):
        """
        Заполнить данные по участникам
        :param widgets_dict: словарь с виджетами данных об участнике и сумме затрат
        """

        for k in widgets_dict:
            self.part_list[self.part_list_widgets.get(k).ids.name.text] = {"Затраты": round(float(self.part_list_widgets.get(k).ids.expenses.text), 2)}

    def calc_debt(self):
        """Рассчитать суммы долга"""

        self.screen.ids.box.clear_widgets()
        # Получить список отсортированных по сумме долга словарей
        self.fill_part_list(self.part_list_widgets)
        sorted_names_by_debt = debt_calculate_by_name(dict(self.part_list))
        all_debts = get_all_debts(dict(self.part_list))

        self.info_text = "\n"
        self.screen.ids.box.add_widget(MDLabel(
            text="Итоги расчетов:",
            halign="center",
            font_style='H6'
        ))

        self.screen.ids.box.add_widget(MDLabel(
            text=f"Общая сумма: {get_total_expenses(dict(self.part_list))}",
            halign="center",
            font_style='H6'
        ))

        self.screen.ids.box.add_widget(MDLabel(
            text=f"Средняя сумма: {get_average_expenses(dict(self.part_list))}",
            halign="center",
            font_style='H6'
        ))

        self.info_text += f"Общая сумма: {get_total_expenses(dict(self.part_list))}"
        self.info_text += f"Средняя сумма: {get_average_expenses(dict(self.part_list))}"

        while all_debts != [0] * len(self.part_list):  # Пока все долги не обнуляться

            # Получить минимальную и максимальную сумму долга
            min_debt, max_debt = sorted_names_by_debt[0][1].get('Долг'), sorted_names_by_debt[-1][-1].get('Долг')

            # Вычислить сумму перевода участника с максимальным долго участнику с минимальным долгом
            transfer_summ = abs(min_debt) if max_debt > abs(min_debt) else max_debt
            if transfer_summ == 0:
                break

            self.screen.ids.box.add_widget(MDLabel(
                text=f"{sorted_names_by_debt[-1][0]} Переводит {sorted_names_by_debt[0][0]} {transfer_summ}",
                halign="center",
                font_style='H6'
            ))

            self.info_text += f"\n{sorted_names_by_debt[-1][0]} Переводит {sorted_names_by_debt[0][0]} {transfer_summ}\n"

            # Обновить суммы долгов
            debt_credit = round((min_debt + max_debt), 2)
            sorted_names_by_debt[0][1]['Долг'] = 0 if max_debt > abs(min_debt) else debt_credit
            sorted_names_by_debt[-1][-1]['Долг'] = 0 if max_debt < abs(min_debt) else debt_credit

            # Обновить данные, перевычислить долги
            participants = sorted_debt(dict(sorted_names_by_debt))
            sorted_names_by_debt = participants
            all_debts = get_all_debts(dict(participants))
        else:
            print("\nВсе долги рассчитаны\n")

        if self.info_text not in ("", "\n", "Расчет не производился"):
            self.screen.ids.tab2.add_widget(
                MDFloatingActionButton(
                    icon='content-copy',
                    md_bg_color=[0.26, 0.40, 0.55, 1],
                    text_color=[1, 1, 1, 1],
                    elevation=0,
                    on_release=self.copy_result,
                    pos=[30, 30]
                )
            )

        self.screen.ids.tabs.switch_tab(self.screen.ids.tab2.text)

    def show_info(self):
        """Открыть диалоговое окно с информацией"""

        info_text_list = [
            '\n1. На вкладке "Участники"\n',
            'ввести количество участников\n',
            '2. Нажать кнопку\n',
            '"Создать таблицу"\n',
            '3. Ввести имена\n',
            'и сумму затрат\n ',
            'для каждого участника\n',
            '4. Нажать Рассчитать\n',
            'После нажатия рассчитать\n,',
            'приложение переключится\n',
            'на вкладку "Расчет"\n',
            'Кнопки "Добавить" и "Удалить"\n',
            'соответственно добавляют\n',
            'и удаляют одну строку\n',
            'для заполнения данных\n'

        ]

        self.info_dialog.content_cls.ids.info_list.clear_widgets()
        for line in info_text_list:
            widget = MDLabel(
                text=line,
                halign="center",
                font_style='Caption'
            )
            self.info_dialog.content_cls.ids.info_list.add_widget(widget)
        self.info_dialog.open()

    def close_info(self, inst):
        """Закрыть окно с информацией"""

        self.info_dialog.dismiss()

    def copy_result(self, inst):
        """Скопировать результаты расчетов в буфер обмена"""

        Clipboard.copy(self.info_text)
        snackbar = Snackbar(
            text='Скопировано',
            snackbar_x="200dp",
            snackbar_y="25dp",
            bg_color=[0.09, 0.59, 0.45, 1]
        )
        snackbar.open()

    @staticmethod
    def close_app():
        """Закрыть приложение"""

        DebtCalculate.get_running_app().stop()
        WindowBase().close()


if __name__ == '__main__':
    DebtCalculate().run()
