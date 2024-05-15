from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, BoundedNumericProperty, NumericProperty, ReferenceListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from debtcalculate import KV
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.core.window import WindowBase
from kivy.clock import Clock
from kivymd.uix.button import MDRoundFlatButton, MDFillRoundFlatButton, MDRectangleFlatButton, MDFloatingActionButton

from kivymd.uix.textfield import MDTextField
from helpers import *
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.core.clipboard import Clipboard
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.metrics import dp

class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemColor(BoxLayout):
    text = StringProperty()
    color = ListProperty()


class MyButton(MDFillRoundFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = [0.26, 0.40, 0.55, 1]
    width = BoundedNumericProperty(
        88, min=88, max=None, errorhandler=lambda x: 88
    )
    height = NumericProperty(100)
    size = ReferenceListProperty(width, height)


class MyTextField(MDTextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = None if self.focus else self._hint_text


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class DebtCalculate(MDApp):

    title = "Сколько должен"
    by_who = 'by anb76ru'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.part_list_widgets = {}
        self.part_list = {}
        self.info_dialog = None
        self.info_text = "Расчет не производился"

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(iterative):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()
        Clock.schedule_once(set_item, 0.1)

    def on_start(self):
        self.screen.ids.box.add_widget(MDLabel(
            text=self.info_text,
            halign="center",
            font_style='H6'
        ))
    
    def build(self):
        return self.screen

    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        '''Called when switching tabs.

        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''

        # instance_tab.ids.label.text = tab_text
        print(f"tab clicked {tab_text}")

    def get_data(self, date):
        self.screen.ids.start_date = date.strftime("%d-%m-%y")

    def on_save(self):
        pass

    def on_cancel(self):
        pass

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
        if not isinstance(participant_count, int):
            self.close_app()
        for i in range(1, participant_count+1):
            row_color = (0.98, 0.98, 0.98, 1)
            widget = ItemColor(color=row_color, text=str(i))
            self.part_list_widgets[f'user_{i}'] = widget
            self.screen.ids.table_list.add_widget(widget)

    def add_row(self):
        row_color = (0.98, 0.98, 0.98, 1)
        widget = ItemColor(color=row_color, text=str(len(self.part_list_widgets) + 1))
        self.part_list_widgets[f'user_{len(self.part_list_widgets) + 1}'] = widget
        self.screen.ids.table_list.add_widget(widget)

    def remove_row(self):
        widget = self.part_list_widgets.pop(f'user_{len(self.part_list_widgets)}')
        self.screen.ids.table_list.remove_widget(widget)

    def clear_text(self):
        self.screen.ids.name.text = ''

    def fill_part_list(self, widgets_dict: dict):
        """
        Заполнить данные по участникам
        :param widgets_dict:
        """

        for k in widgets_dict:
            self.part_list[self.part_list_widgets.get(k).ids.name.text] = {"Затраты": round(float(self.part_list_widgets.get(k).ids.expenses.text), 2)}

    def calc_debt(self):
        """

        :param part_dict:
        :return:
        """
        self.screen.ids.box.clear_widgets()
        # Получить список отсортированных по сумме долга словарей
        self.fill_part_list(self.part_list_widgets)
        sorted_names_by_debt = debt_calculate_by_name(dict(self.part_list))
        all_debts = get_all_debts(dict(self.part_list))

        self.info_text = "\n"
        self.info_text += f"\nОбщая сумма: {get_total_expenses(dict(self.part_list))}\n"
        self.info_text += f"\nСредняя сумма: {get_average_expenses(dict(self.part_list))}\n"

        while all_debts != [0] * len(self.part_list):  # Пока все долги не обнуляться

            # Получить минимальную и максимальную сумму долга
            min_debt, max_debt = sorted_names_by_debt[0][1].get('Долг'), sorted_names_by_debt[-1][-1].get('Долг')

            # Вычислить сумму перевода участника с максимальным долго участнику с минимальным долгом
            transfer_summ = abs(min_debt) if max_debt > abs(min_debt) else max_debt
            if transfer_summ == 0:
                break
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

        self.screen.ids.box.add_widget(MDLabel(
            text="Итоги расчетов: \n",
            halign="center",
            font_style='H6'
        ))

        self.screen.ids.box.add_widget(MDLabel(
            text=f"\n{self.info_text}",
            halign="center",
            font_style='H6'
        ))
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

        info_txt = """
        Как работать с приложением:\n
        1. На вкладке "Люди" ввести 
        количество участников
        
        2. Нажать кнопку 
        "Создать таблицу"
        
        3. Ввести имена и сумму затрат
         для каждого участника
        
        4. Нажать Рассчитать
        
        После нажатия рассчитать,
        приложение переключится 
        на вкладку "Расчет"
        
        Кнопки "Добавить" и "Удалить" 
        соответственно 
        добавляют и удаляют
        одну строку 
        для заполнения данных
        """

        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title="Information",
                text=info_txt,
                buttons=[
                    MyButton(text="CLOSE", on_release=self.close_info)
                ],
                size_hint=(1, 1)
            )
        self.info_dialog.open()

    def close_info(self, inst):
        """Закрыть окно с информацией"""

        self.info_dialog.dismiss()

    def copy_result(self, inst):
        """"""

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
        DebtCalculate.get_running_app().stop()
        WindowBase().close()


if __name__ == '__main__':
    DebtCalculate().run()
