from kivy.app import App
from kivy.uix.button import Button


class DebtCalculate(App):

    def build(self):
        return Button(text='Hello world')


if __name__ == '__main__':
    DebtCalculate().run()
