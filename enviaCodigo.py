import serial
import time


def run_micropython_code(port, main3):
    leerparaESP32=main3()

    with serial.Serial(port, 115200, timeout=1) as ser:
        ser.write(b'\x03')  # Envía un Ctrl-C para interrumpir cualquier programa en ejecución
        time.sleep(0.5)
        ser.write(b'\r\x01')  # Ingresa al modo raw REPL
        ser.write(b'\x04')  # Envía un Ctrl-D para hacer un soft reset
        time.sleep(0.5)
        ser.write(leerparaESP32.encode('utf-8'))  # Envía el código MicroPython
        ser.write(b'\x04')  # Envía un Ctrl-D para ejecutar el código
        time.sleep(0.5)

        while True:
            output = ser.readline().decode('utf-8').strip()
            if output == "":
                break
            print(output)

        ser.write(b'\r\x02')  # Sale del modo raw REPL

    
