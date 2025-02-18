import socket

def send_file(filename, host='172.31.11.193', port=40000):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's port
    client_socket.connect((host, port))
    print(f"Connected to {host}:{port}")

    # Send the file
    with open(filename, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.sendall(data)

    print("File sent successfully.")
    client_socket.close()

if __name__ == "__main__":
    send_file('twitter.svg')
