import speech_recognition as sr
import pyttsx3
class Speak:
    def Command(self):
        self.recognizer=sr.Recognizer()
        self.microphone=sr.Microphone()
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
            
        return cmd