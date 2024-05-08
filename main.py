from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, BoundedNumericProperty, NumericProperty, ReferenceListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from debtcalculate import KV
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase
from kivymd.font_definitions import fonts
from kivy.core.window import WindowBase
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivymd.uix.picker import MDDatePicker
import datetime
from kivymd.uix.textfield import *
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.textfield import MDTextField
from helpers import *
from kivymd.uix.label import MDLabel


class Tab(MDFloatLayout, MDTabsBase):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass

class ItemColor(BoxLayout):
    text = StringProperty()
    color = ListProperty()

class MyButton(MDRoundFlatButton):
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

    title = "Debt Calculate"
    by_who = 'by anb76ru'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [{"icon": "git", "text": f"Item {i}"} for i in range(2, 11)]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position="auto",
            width_mult=4
        )
        self.menu.bind(on_release=self.set_item)

        self.part_list_widgets = {}
        self.part_list = {}

        #self.date_dialog = MDDatePicker(callback=self.get_data)
        #self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)

    def set_item(self, instance_menu, instance_menu_item):
        def set_item(iterative):
            self.screen.ids.payment_type.text = instance_menu_item.text
            instance_menu.dismiss()
        Clock.schedule_once(set_item, 0.1)
    
    def build(self):
        return self.screen

    def on_start(self):
        icons_item = {
            "folder": "My files",
            "account-multiple": "Shared with me",
            "star": "Starred",
            "history": "Recent",
            "checkbox-marked": "Shared with me",
            "upload": "Upload",
            "shield-sun": "Dark/Light",
            'exit-to-app': "Exit",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

        # self.screen.ids.table_list.clear_widgets()
        # participant_count = self.get_count_participant()
        # for i in range(participant_count):
        #     row_color = (1, 1, 2, 1)
        #     # if i%2 != 0:
        #     #     row_color = (1, 1, 1, 1)
        #     self.screen.ids.table_list.add_widget(
        #        ItemColor(color=row_color, text=str(i))
        #    )
        # for name_tab in list(md_icons.keys())[10:20]:
        #     self.root.ids.tabs.add_widget(Tab(text=f'{name_tab}'))

        # for icon_name, name_tab in icons_item.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(text=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref] {name_tab}")
        #     )

        # for i in range(5):
        #     self.root.ids.scroll.add_widget(MDTextField(
        #                                                 hint_text='Enter expense'))
        #     self.root.ids.scroll2.add_widget(MDTextField(text='Enter expense'))

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

        count_text = self.screen.ids.participant_count.text
        return int(count_text) if count_text else 0

    def create_table_to_add_data(self):
        """Создать таблицу для заполнения данных"""

        self.screen.ids.table_list.clear_widgets()
        participant_count = self.get_count_participant()
        for i in range(1, participant_count+1):
            row_color = (0.98, 0.98, 0.98, 1)
            # if i%2 != 0:
            #     row_color = (1, 1, 1, 1)
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

        while all_debts != [0] * len(self.part_list):  # Пока все долги не обнуляться

            # Получить минимальную и максимальную сумму долга
            min_debt, max_debt = sorted_names_by_debt[0][1].get('Долг'), sorted_names_by_debt[-1][-1].get('Долг')

            # Вычислить сумму перевода участника с максимальным долго участнику с минимальным долгом
            transfer_summ = abs(min_debt) if max_debt > abs(min_debt) else max_debt
            print(f"\n{sorted_names_by_debt[-1][0]} Переводит {sorted_names_by_debt[0][0]} {transfer_summ}")
            self.screen.ids.box.add_widget(MDLabel(
                text=f"\n{sorted_names_by_debt[-1][0]} Переводит {sorted_names_by_debt[0][0]} {transfer_summ}",
                halign="center",
                font_style='H6'
            ))

            # Обновить суммы долгов
            debt_credit = min_debt + max_debt
            sorted_names_by_debt[0][1]['Долг'] = 0 if max_debt > abs(min_debt) else debt_credit
            sorted_names_by_debt[-1][-1]['Долг'] = 0 if max_debt < abs(min_debt) else debt_credit

            # Обновить данные, перевычислить долги
            participants = sorted_debt(dict(sorted_names_by_debt))
            sorted_names_by_debt = participants
            all_debts = get_all_debts(dict(participants))
        else:
            print("\nВсе долги рассчитаны\n")



    @staticmethod
    def close_app():
        MDApp.get_running_app().on_stop()
        WindowBase().close()


DebtCalculate().run()
