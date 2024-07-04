
import bard
import pyttsx3
import speech_recognition

# Define a function to listen for user input.
def listen_for_user_input():
    with speech_recognizer.listen(timeout=5) as source:
        audio = speech_recognizer.listen(source)

    # Transcribe the audio to text.
    try:
        user_input = speech_recognizer.recognize_google(audio)
    except speech_recognition.UnknownValueError:
        user_input = None

    return user_input

# Define a function to speak to the user.
def speak_to_user(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Create a Bard client.
bard_client = bard.Client(api_token='bgiWsvYaySRsNwZS2rqhBQMulPAhHGGUhxkk9MABE0_21vno0BKWvYXI2-XV-JOUmaPvDA')

# Initialize the speech recognition engine.
speech_recognizer = speech_recognition.Recognizer()

# Initialize the text-to-speech engine.
tts_engine = pyttsx3.init()



# Start the main loop.
while True:
    # Listen for user input.
    user_input = listen_for_user_input()

    # If the user input is not empty, send it to Bard and get a response.
    if user_input is not None:
        bard_response = bard_client.generate(text=user_input)

        # Speak the Bard response to the user.
        speak_to_user(bard_response)
