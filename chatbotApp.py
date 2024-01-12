from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from openai import OpenAI
import speech_recognition as sr



client = OpenAI(api_key='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')
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
class FirstLayout(GridLayout):
   def __init__(self, **kwargs):
      super(FirstLayout,self).__init__(**kwargs)
      self.cols = 1
      #user input
      self.add_widget(Label(text = "User:"))
      self.message = TextInput(multiline = True)
      self.add_widget(self.message)
      #send button
      self.send = Button(text = "Send",font_size = 25)
      self.send.bind(on_press = self.press)
      self.add_widget(self.send)
      #audio button
      self.audio = Button(text = "say something", font_size = 15)
      self.audio.bind(on_press = self.voice_to_text)
      self.add_widget(self.audio)

   def press(self,instance):
       if self.message.text:
        messages.append(
            {"role": "user", "content": self.message.text},
        )
        self.chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    
        self.reply = self.chat.choices[0].message.content
        self.add_widget(Label(text =f"Bot: {self.reply}"))
        messages.append({"role": "assistant", "content": self.reply})

       self.message.text=""
   def voice_to_text(self,instance):
    # Initialize the recognizer
        self.recognizer = sr.Recognizer()

    # Capture audio from the microphone
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.audio = self.recognizer.listen(source, timeout=5)

        try:
        # Recognize speech using Google Web Speech API
            self.text = self.recognizer.recognize_google(self.audio)
            self.message.text = self.text
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
         print(f"Could not request results from Google Web Speech API; {e}")



class Chatbot(App):
   def build(self):
      return FirstLayout()

Chatbot().run()