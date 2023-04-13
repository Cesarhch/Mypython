import network
import socket

def setup_ap(ssid, password):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA2_PSK)
    while not ap.active():
        pass
    print('AP creado. SSID:', ssid, 'Contraseña:', password)

def start_server(port=80):
    addr = socket.getaddrinfo('0.0.0.0', port)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Escuchando en', addr)
    return s

def main():
    setup_ap("ESP32", "my12345678")
    s = start_server()

    while True:
        conn, addr = s.accept()
        print("Conexion desde", addr)
        request = conn.recv(1024)
        print("Request:", request)

        response = "HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n"
        response += "<html><body><h1>Datos recibidos:</h1>"
        response += str(request)
        response += "</body></html>"

        conn.send(response)
        conn.close()

main()


