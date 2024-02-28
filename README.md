#Weather Microservice

The weather microservice is a Python-based microservice that can provide the weather and some details.

This microservice can obtain a specified location's temperature, humidity, and description. 
Furthermore, it works over a socket request, allowing it to hold multiple requests simultaneously.

To utilize this service, obtain the code and an API key for the OpenWeatherMap and your local machine IP address, 
and substitute it into the API key portion of the code and the HOST portion of the code, if the sample key is not working. 
Furthermore, run the client program allowing for it to be set up on a port on the local machine, and then run the client side.
After running these text should pop up in the console for a location, where a city can be entered, thus returning the details.

Communication Contract
I am utilizing an API from the OpenWeatherMap to allow for the data to be collected. This is phenomenon that will not change 
throughout the development of this microservice. 
