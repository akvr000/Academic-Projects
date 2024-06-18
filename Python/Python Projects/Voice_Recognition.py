import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from microphone
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # Recognize speech using the default Google Speech Recognition API
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand what you just said.")
    except sr.RequestError as e:
        print("Error with the service, Please try again later; {0}".format(e))

# Call the function to recognize speech
recognize_speech()
