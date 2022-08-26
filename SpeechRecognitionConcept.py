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
    # Create recognizer and microphone instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    # Prompt User
    print("speak")
    # Trigger recognize_speech_from_mic function. Store audio output in command variable
    command=recognize_speech_from_mic(recognizer, microphone)
    # Print audio output
    print("You said: {}".format(command))
    # Logic for Response
    if "beach" in command:
        print("Check The Weather")
        print("Sun screen")
        print("Beach Towels")
        print("Wallet")
        print("Sandles")
        