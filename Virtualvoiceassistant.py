import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process the recognized speech
def process_speech(phrase):
    phrase = phrase.lower()
    if "hello" in phrase:
        speak("Hello! How can I assist you?")
    elif "your name" in phrase:
        speak("My name is Assistant.")
    elif "thank you" in phrase:
        speak("You're welcome!")
    else:
        speak("I'm sorry, I didn't understand. Can you please repeat?")

# Main program loop
while True:
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        phrase = recognizer.recognize_google(audio)
        print("You said:", phrase)
        process_speech(phrase)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service:", str(e))
