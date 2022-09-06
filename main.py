from kivy.lang import Builder
from kivymd.app import MDApp

import speech_recognition as sr
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices,', voices[1].id)
recognizer=sr.Recognizer()


KV = '''
MDScreen:
    MDRaisedButton:
        text: "Momo"
        on_release: app.switch_theme_style()
        pos_hint: {"center_x": .5, "center_y": .5}
'''


class Momo(MDApp):
    def build(self, **kwargs):
        if self.theme_cls.primary_palette == "Red":
            engine.say("Red")
            engine.runAndWait()
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(KV)

    def switch_theme_style(self):
        listening = True
        engine.say("Speak")
        engine.runAndWait()
        recognizer=sr.Recognizer()
        microphone=sr.Microphone()
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
        if "school" in cmd:
                # testing
            engine.say("check the weather\nbring wallet.\n.full sail badge.\nschool bag.\nlap top.\ncharger.\nglasses.\npen.\nnotebook.\nDid you get everything?")
            engine.runAndWait()
        elif "birthday" in cmd:
                # testing
            engine.say("Check the weather. Birthday Card. Wallet. Make sure to say happy birthday and to take plenty of pictures. Did you get everything?")
            engine.runAndWait()
     




        


Momo().run()