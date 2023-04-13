import network

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Mired', password='Mi12345678')
ap.ifconfig(('192.168.0.1', '255.255.255.0', '192.168.0.1', '8.8.8.8'))

print(ap.ifconfig())
