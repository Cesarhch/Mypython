import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("Dime que necesitas...")
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    # Listen for audio input
    audio = r.listen(source)

    try:
        # Convert audio to text
        text = r.recognize_google(audio, language="es-ES")
        print(f"He entendido: {text}")
        #Comprobar si reconoce una instruccion
        keyword='enciende el led'
        if keyword in text.lower():
            print('entiendo la instruccion')
        else:
            print('lo siento, no he entendido la instruccion')
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
