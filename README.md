# Flask Web Application for Hue Bridge Control
This web application is built using Flask and allows for control of lights connected to a Philips Hue Bridge through a web interface. The lights can be grouped and controlled separately using the Bridge class.

## Getting Started
Make sure you have Python 3.7 or later installed on your system.
Install the required dependencies by running:
- pip install phue
- pip install Flask
Replace BRIDGE_IP and USERNAME in the `utils/Bridge` class with the IP address and username of your Philips Hue Bridge.
Run the application by navigating to the project root in command prompt and executing 'flask run'.
Access the application by navigating to http://localhost:5000 in your web browser.

## Functionality
The application has several routes that can be accessed to control the lights:

- /on/<string:room>: Turns on the lights in the specified room.
- /off/<string:room>: Turns off the lights in the specified room.
- /brightness/<string:room>/<int:level>: Sets the brightness of the lights in the specified room to the specified level (0-254).
- /color/<string:room>/<int:r>/<int:g>/<int:b>: Sets the color of the lights in the specified room to the specified RGB color.
- The sort_lights function is used to group the lights based on their location.

The rgb_to_xy function is used to convert RGB colors to the xy colorspace used by the Philips Hue Bridge.

The Bridge class is used to control the lights connected to the Philips Hue Bridge, which includes methods for turning lights on and off, setting brightness, color, color temperature, alert, and effect.

## Dependencies
- flask
- phue
- utils.Bridge
- utils.helpers

## Additional notes
The Bridge class is a subclass of the phue library's Bridge class and extends its functionality to include additional methods for controlling the lights.
The web application is built using Flask and the routes are defined using the Flask @app.route decorator.
The index route renders the index.html template and serves as the landing page of the application.
The routes handle HTTP POST requests and return a 204 No Content status code.
The rgb_to_xy function is used to convert RGB colors to the xy colorspace used by the Philips Hue Bridge.
