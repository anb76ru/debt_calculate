from kivymd.uix.list import MDList
from kivymd.uix.tab import MDTabsBase
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.theming import ThemableBehavior
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.properties import StringProperty, ListProperty
from kivy.properties import BoundedNumericProperty, NumericProperty, ReferenceListProperty


class Tab(MDFloatLayout, MDTabsBase):
    """Вкладка"""
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class InfoContent(ScrollView):
    pass


class MemberRow(BoxLayout):
    text = StringProperty()
    color = ListProperty()


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class FlatButton(MDFillRoundFlatButton):
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


class DrawerList(ThemableBehavior, MDList):
    pass
