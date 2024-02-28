import socket

#methods servers
def fetch_weather(location):
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(location.encode("utf-8"))
        data = client_socket.recv(1024).decode("utf-8")
        print(f"Received weather data: {data}")

if __name__ == "__main__":
    location = input("Enter location: ")
    fetch_weather(location)
