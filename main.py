from Speak import Speak
from Weather import Weather
from Prompt import Prompt
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCardSwipe
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
import speech_recognition as sr
import pyttsx3
import os


KV = '''
<SwipeToDeleteItem>:
    size_hint_y: None
    height: content.height

    MDCardSwipeLayerBox:
        padding: "8dp"

        MDIconButton:
            icon: "trash-can"
            pos_hint: {"center_y": .5}
            on_release: app.remove_item(root)

    MDCardSwipeFrontBox:

        OneLineListItem:
            id: content
            text: root.text
            _no_ripple_effect: True
MDScreen:
    MDBoxLayout:
        id: box
        orientation: "vertical"
        MDTopAppBar:
            elevation: 4
            title: "Destination: Beach"

        MDScrollView:

            MDList:
                id: md_list
                padding: 0


        # Will always be at the bottom of the screen.
        MDBottomAppBar:

            MDTopAppBar:
                icon: "microphone"
                on_action_button: app.switch_theme_style(self.icon)
                type: "bottom"

'''

class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.screen = Builder.load_string(KV)

    def build(self):
        self.voice = True
        return self.screen
    def remove_item(self, instance):
        self.screen.ids.md_list.remove_widget(instance)

    def switch_theme_style(self, instance):
        self.engine=pyttsx3.init()
        self.screen.ids.md_list.add_widget(
        SwipeToDeleteItem(text=f"{Weather.forcast(self)} degrees") 
        )
        self.engine.say("Speak")
        self.engine.runAndWait()
        cmd = Speak.Command(self)
        response = Prompt.prompt_model(self, cmd)
        for i in range(10):
            self.screen.ids.md_list.add_widget(
            SwipeToDeleteItem(text=f"{response[i]}")
            )
        return self

if __name__ == '__main__':
    Test().run()
