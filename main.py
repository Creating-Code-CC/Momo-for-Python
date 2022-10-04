from email.mime import application
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.card import MDCardSwipe
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
import speech_recognition as sr
import pyttsx3
import requests
import os
import openai
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=dfe4fcca2e4626bac10b82115b7b5415" + "&q=Orlando"
response = requests.get(complete_url)
x = response.json()
y = x["main"]
current_temperature = y["temp"]
celsius = current_temperature - 273.15
fahrenheit = celsius * (9/5) + 32
predictedWeather= round(fahrenheit)
weatherpromt=" The temperature is " + str(predictedWeather) + " degrees"
beachList = [weatherpromt,"Bathing Suit","Drinks", "Snacks", "Hat", "Beach", "Towel", "Sunglasses", "Sunscreen", "Water", "Sandles", "Wallet", "Did you get everything?"]
schoolList = [weatherpromt,"Full Sail Badge","Laptop","Laptop Charger","Phone","Wallet","Glasses","Pen","Did you get everything?"]
birthdayList= [weatherpromt,"Birthday Card","Wallet","Make sure to say happy birthday and to take plenty of pictures","Did you get everything?"]
fairList = [weatherpromt,"Cash for tickets, games and concession stands","Hand sanitizer","Wallet", "Did you get everything?"]
movieList = [weatherpromt,"Cash for tickets, popcorn and Soda","Movie Tickets","Sweater","Wallet","Did you get everything?"]
footballList = [weatherpromt,"Football tickets","Team Jersey","Bring a friend","Props","insect repellent","Wallet","Did you get everything?"]

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
            title: "Momo"
            right_action_items:

        MDScrollView:

            MDList:
                id: md_list
                padding: 0


        # Will always be at the bottom of the screen.
        MDBottomAppBar:

            MDTopAppBar:
                icon: "microphone"
                left_action_items: [["volume-off", lambda x: app.disable_voice()]]
                on_action_button: app.switch_theme_style(self.icon)
                type: "bottom"

'''
openai.api_key = ("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")
response = openai.Completion.create(model="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)

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

    # def on_start(self):
    #     for i in range(8):
    #         self.screen.ids.md_list.add_widget(
    #             SwipeToDeleteItem(text=f"{footballList[i]}")
    #          )

    def switch_theme_style(self, instance):
        self.engine=pyttsx3.init()
        self.recognizer=sr.Recognizer()
        self.microphone=sr.Microphone()
        self.engine.say("Speak")
        self.engine.runAndWait()
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(self.recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.audio = self.recognizer.listen(source)
    
        try:
            cmd=self.recognizer.recognize_google(self.audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            cmd = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            cmd="Unable to recognize speech"
        if "school" in cmd:
                # testing
            for i in range(9):
                self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"{schoolList[i]}")
             )
            if self.voice == True:
                self.engine.say(weatherpromt + ",   bring wallet. full sail badge. school bag. lap top. charger. glasses. pen. notebook. Did you get everything?")
                self.engine.runAndWait()
        elif "birthday" in cmd:
                # testing
            for i in range(5):
                self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"{birthdayList[i]}")
             )
            if self.voice == True:
                self.engine.say(weatherpromt + ",  Birthday Card. Wallet. Make sure to say happy birthday and to take plenty of pictures. Did you get everything?")
                self.engine.runAndWait()
        elif "beach" in cmd:
                # testing
            for i in range(13):
                self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"{beachList[i]}"))
            if self.voice == True:
                self.engine.say(weatherpromt + ",  Bathing Suit. Drinks. Snacks. Hat. Beach Towel. Sunglasses. Sunscreen. Water. Sandles. Wallet. Did you get everything?")
                self.engine.runAndWait()
        elif "fair" in cmd:
                # testing
            for i in range(5):
                self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"{fairList[i]}")
             )
            if self.voice == True:
                self.engine.say(weatherpromt + ",  Check the weather. Cash for games and concession stands. Hand sanitizer. Wallet. Did you get everything?")
                self.engine.runAndWait()
        elif "movies" in cmd:
            for i in range(6):
                self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"{movieList[i]}")
             )
                # testing
            if self.voice == True:
                self.engine.say(weatherpromt + ",  Popcorn and Soda Money. Movie Tickets. Sweater. Wallet. Did you get everything?")
                self.engine.runAndWait()
        elif "football" in cmd:
            for i in range(8):
                self.screen.ids.md_list.add_widget(
                SwipeToDeleteItem(text=f"{footballList[i]}")
             )
                # testing
            if self.voice == True:
                self.engine.say(weatherpromt + ", Football tickets. Team Jersey. Bring a friend. Props.insect repellent. Wallet. Did you get everything?")
                self.engine.runAndWait()

    def disable_voice(self):
        if self.voice == True:
            self.voice = False
        else:
            self.voice = True


Test().run()
