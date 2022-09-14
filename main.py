from email.mime import application
from kivy.lang import Builder

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
beach = weatherpromt + ",  Bathing Suit. Drinks. Snacks. Hat. Beach Towel. Sunglasses. Sunscreen. Water. Sandles. Wallet. Did you get everything?"
KV = '''
MDBoxLayout:

    # Will always be at the bottom of the screen.
    MDBottomAppBar:

        MDTopAppBar:
            icon: "microphone"
            on_action_button: app.switch_theme_style(self.icon)
            type: "bottom"

        MDScrollView:
            MDList:
                id: md_list
                padding: 0
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

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
            self.engine.say(weatherpromt + ",   bring wallet. full sail badge. school bag. lap top. charger. glasses. pen. notebook. Did you get everything?")
            self.engine.runAndWait()
        elif "birthday" in cmd:
                # testing
            self.engine.say(weatherpromt + ",  Birthday Card. Wallet. Make sure to say happy birthday and to take plenty of pictures. Did you get everything?")
            self.engine.runAndWait()
        elif "beach" in cmd:
                # testing
            MDLabel(text="Hello", pos_hint={"center_x": .5, "center_y": .5})
            self.engine.say(weatherpromt + ",  Bathing Suit. Drinks. Snacks. Hat. Beach Towel. Sunglasses. Sunscreen. Water. Sandles. Wallet. Did you get everything?")
            self.engine.runAndWait()
        elif "fair" in cmd:
                # testing
            self.engine.say(weatherpromt + ",  Check the weather. Cash for games and concession stands. Hand sanitizer. Wallet. Did you get everything?")
            self.engine.runAndWait()
        elif "movies" in cmd:
                # testing
            self.engine.say(weatherpromt + ",  Popcorn and Soda Money. Movie Tickets. Sweater. Wallet. Did you get everything?")
            self.engine.runAndWait()


Test().run()
