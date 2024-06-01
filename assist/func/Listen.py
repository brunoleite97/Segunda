import speech_recognition as sr

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.dynamic_energy_threshold = True
recognizer.dynamic_energy_adjustment_damping = 0.15
recognizer.dynamic_energy_ratio = 1.5
recognizer.pause_threshold = 0.8
recognizer.operation_timeout = None
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5

def Listen() ->str|None:
    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio_data = recognizer.listen(source)

        try:
            print("Recognizing...")

            text = recognizer.recognize_google(audio_data)

            print(f"Speech recognized: {text}")
            return text
        
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        
        except sr.RequestError as e:
            print(f"Error: {e}")
            return None