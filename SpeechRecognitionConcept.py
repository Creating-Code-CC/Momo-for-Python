import speech_recognition as sr
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



if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("speak")
    command=recognize_speech_from_mic(recognizer, microphone)
    print("You said: {}".format(command))
    if "beach" in command:
        print("Check The Weather")
        print("sunscreen")
        print("beach towels")
        print("wallet")
        print("sandles")