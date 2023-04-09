import serial
import time
import subprocess
import speech_recognition as sr

def upload_file_to_esp32(port, filename):
    # Define the baud rate
    baud_rate = 115200

    # Open the serial port
    ser = serial.Serial(port, baud_rate, timeout=1)

    # Wait for the ESP32 device to initialize
    time.sleep(2)

    # Use ampy to transfer the file to the device
    subprocess.run(['/Users/cesarhernandez/Library/Python/3.9/bin/ampy', '--port', port, 'put', filename])

def reset_esp32(port):
    # Use esptool.py to reset the ESP32 device
    subprocess.run(['/Users/cesarhernandez/Library/Python/3.9/bin/ampy', '--port', port, 'run', filenamereset])

port = '/dev/tty.usbserial-0001'  
filename = '/users/cesarhernandez/Desktop/Mypython/main.py'
filenamereset = '/users/cesarhernandez/Desktop/Mypython/reset.py'

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
        keyword='cambia el led'
        if keyword in text.lower():
            print('entiendo la instruccion')
            upload_file_to_esp32(port, filename)
            #reset_esp32(port)
        else:
            print('lo siento, no he entendido la instruccion')
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
