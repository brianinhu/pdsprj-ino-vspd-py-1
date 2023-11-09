"""autopep8"""

import serial

ARDUINO_PORT = 'COM2'
BAUD_RATE = 9600

with serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=2) as arduino:
    print("Presione 1 para Encender y 0 para Apagar el LED:  ")

    while True:
        datousuario = input("Ingrese su elección (1/0): ")

        if datousuario == '1' or datousuario == '0':
            arduino.write(datousuario.encode())
            print(f"LED {'Encendido' if datousuario == '1' else 'Apagado'}")
        else:
            print("Entrada no válida. Por favor, ingrese 1 o 0.")
