import kivy
# kivy.app = function App 'uppercase' = class
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
# OOP Inheritance


class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Momo'))

class MoMo(App):
    def build(self):
        return MainScreen()

if __name__ == "__main__":
        MoMo().run()