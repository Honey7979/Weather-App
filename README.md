# Weather App

This Python application fetches the current weather information for a specified city and displays it with a dynamically changing background based on the weather conditions. The application uses Tkinter for the GUI and the OpenWeatherMap API for fetching weather data.

## Table of Contents
- Features
- Installation
- Usage
- Files and Structure
- Dependencies
- Notes
- License

## Features
- Fetches current weather data for a specified city.
- Displays temperature, weather description, humidity, and wind speed.
- Dynamically changes the background image based on the weather conditions.

## Installation

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. **Create a Virtual Environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Libraries:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up OpenWeatherMap API Key:**
    - Replace `'e3cb3c930ab6454130e91932140a0679'` in `weather.py` with your OpenWeatherMap API key.

5. **Create Weather Images Directory:**
    - Ensure you have a directory named `Weather_Images` with appropriate weather condition images (e.g., `default.png`, `sunny.png`, `rainy.png`, etc.).

## Usage

Run the main application script to start the weather app.

```sh
python main.py
```
### Example
1. Enter a city name in the input field.
2. Click on "Get Weather Report".
3. View the current weather information and the dynamically changing background.

## Files and Structure
weather-app/
│
├── Weather_Images/
│   ├── default.png
│   ├── sunny.png
│   ├── rainy.png
│   └── ... (other weather condition images)
│
├── main.py
├── weather.py
├── requirements.txt
└── README.md

`main.py`
The main script to run the weather application. It sets up the GUI using Tkinter, handles user inputs, fetches weather data, and updates the display.

`weather.py`
Contains the function fetch_weather_data(city) that interacts with the OpenWeatherMap API to get the weather data for the specified city.

`requirements.txt`
A list of required Python libraries. Ensure these dependencies are installed for the application to work correctly.

`README.md`
The file you are currently reading, providing an overview and instructions for the project.

## Dependencies

* **tkinter:** Standard Python interface to the Tk GUI toolkit.
* **Pillow:** Python Imaging Library (PIL) fork for opening, manipulating, and saving image files.
* **requests:** Library for making HTTP requests (install if not included).
* **threading:** For running the weather fetch function in a separate thread.

### Install these dependencies using the following command:

```sh
pip install -r requirements.txt
```
## Notes
* The script uses threading to avoid blocking the GUI while fetching weather data.
* The background images should match the weather descriptions returned by the API for accurate display.

