import socket
import requests

#method
def get_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_data = {
            "temperature": f"{data['main']['temp']}°C",
            "humidity": f"{data['main']['humidity']}%",
            "description": data['weather'][0]['description'].capitalize()
        }
        return weather_data
    else:
        print(f"Error fetching weather data: {data['message']}")
        return None

def serve_forever():
    HOST = '127.0.0.1'
    PORT = 65432
    API_KEY = "bd5e378503939ddaee76f12ad7a97608"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected to {addr}")
                while True:
                    location = conn.recv(1024).decode("utf-8")
                    if not location:
                        break
                    weather_data = get_weather_data(API_KEY, location)
                    if weather_data:
                        conn.sendall(str(weather_data).encode("utf-8"))
                    else:
                        conn.sendall(b"Error fetching weather data")
                    print(f"Sent weather data for {location}")

if __name__ == "__main__":
    serve_forever()