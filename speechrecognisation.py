import speech_recognition as sr

def voice_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

# Call the function to get the text from the voice input
result_text = voice_to_text()

# Display the result
if result_text:
    print("Text from voice:")
    print(result_text)
