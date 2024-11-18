import socket

# Network dictionary
NETWORK = {
    '192.168.29.01': 'AC:12:03:2E:70:9A',
    '192.168.29.02': 'AC:12:03:2E:70:9B',
    '192.168.29.03': 'AC:12:03:2E:70:9C',
    '192.168.29.04': 'AC:12:03:2E:70:9D',
    '192.168.29.05': 'AC:12:03:2E:70:9E',
    '192.168.29.06': 'AC:12:03:2E:70:9F',
}

SERVER_IP = '127.0.0.1'
SERVER_PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen()
    print("ARP server is listening...")

    # Keep the server running
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                ip = conn.recv(1024).decode('utf-8')
                if not ip: break
                mac = NETWORK.get(ip, None)
                response = mac if mac else 'Not Found'
                print(f"Received ARP request for IP: {ip}. Responded with: {response}")
                conn.sendall(response.encode('utf-8'))