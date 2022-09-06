import kivy
from kivymd.app import MDApp
from kivy.base import Builder
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import pyttsx3
import speech_recognition as sr

kivy - '''
        MDScreen
'''

engine = pyttsx3.init()
def recognize_speech_from_mic(recognizer, microphone):

    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        cmd=recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        cmd = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        cmd="Unable to recognize speech"
    return cmd

class Momo(App):
    def build(self, **kwargs):
        self.Window = GridLayout()
        self.Window.cols = 1
        self.Logo = Label(text="Momo")
        self.Window.add_widget(self.Logo)
        self.Speak = Button(text="Speak")
        self.Speak.bind(on_press=self.callback)
        self.Window.add_widget(self.Speak)
        return self.Window

    def callback(self, instance):
        self.Speak.text = "Listening"
        recognizer=sr.Recognizer()
        microphone=sr.Microphone()
        cmd=recognize_speech_from_mic(recognizer, microphone)
        self.command= Label(text="You said: {}".format(cmd))
        self.Window.add_widget(self.command)
        if "school" in cmd:
                # testing
            engine.say("check the weather\nbring wallet.\n.full sail badge.\nschool bag.\nlap top.\ncharger.\nglasses.\npen.\nnotebook.\nDid you get everything?")
            engine.runAndWait()
            self.response=Label(text="check the weather\nbring wallet.\n.full sail badge.\nschool bag.\nlap top.\ncharger.\nglasses.\npen.\nnotebook.\nDid you get everything?")
            self.Window.add_widget(self.response)

if __name__ == "__main__":  # run() triggers the class MoMo(App)
        Momo().run()