from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout




class Example(MDApp):
    data_tables = None


    def build(self):


        self.input_text1 = MDTextField(hint_text="No helper text")

        # layout = MDFloatLayout()  # root layout
        layout = MDGridLayout(cols = 1,
                              rows= 4,
                              )  # root layout

        layout.add_widget(MDGridLayout(
                              cols = 6,
                              rows= 4,
                              spacing= 10,
                              )
        )
        layout.add_widget(self.input_text1)







        # Creating control buttons.
        button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )

        # for button_text in ["Add row", "Remove row"]:
        #     button_box.add_widget(
        #         MDRaisedButton(
        #             text=button_text, on_release=self.on_button_press
        #         )
        #     )





        # Create a table.
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=False,
            column_data=[
                ("No.", dp(30)),
                ("Column 1", dp(40)),
                ("Column 2", dp(40)),
                ("Column 3", dp(40)),
            ],
            row_data=[('1', '1', "2", "2"), ('1', '1', "2", "2")]
        )
        self.data_tables.row_data.append((MDTextField(helper_text='123'), MDTextField(helper_text='123'), MDTextField(helper_text='123'), MDTextField(helper_text='123')))
        # Adding a table and buttons to the toot layout.
        # layout.add_widget(input_text)

        layout.add_widget(self.data_tables)
        layout.add_widget(button_box)

        # print(input_text)

        return layout

    def on_button_press(self, instance_button: MDRaisedButton) -> None:
        """Called when a control button is clicked."""

        try:
            {
                "Add row": self.add_row, "Remove row": self.remove_row,
            }[instance_button.text]()
        except KeyError:
            pass

    def add_row(self) -> None:
        last_num_row = int(self.data_tables.row_data[-1][0])
        self.data_tables.add_row((str(last_num_row + 1), "1", "2", "3")) # Should I add the values of the input text here?

    def remove_row(self) -> None:
        if len(self.data_tables.row_data) > 1:
            self.data_tables.remove_row(self.data_tables.row_data[-1])




Example().run()