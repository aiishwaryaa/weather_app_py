# Weather App - Flask Version

A weather application built with Python Flask that displays weather information for cities around the world.

## Features

- Search for weather by city name
- Display current temperature, humidity, and wind information
- Show sunrise and sunset times
- Responsive design with Bootstrap
- RESTful API endpoints

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## API Endpoints

- `GET /` - Main page with search functionality
- `GET /weather/<city>` - Display weather for a specific city
- `GET /api/weather/<city>` - JSON API endpoint for weather data

## Project Structure

```
Weather/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── index.html        # Main page template
│   ├── weather.html      # Weather display template
│   └── error.html        # Error page template
└── static/               # Static files (CSS, images)
    ├── style.css         # Custom styles
    ├── 1.png            # Temperature icon
    ├── 2.png            # Humidity icon
    └── 3.png            # Wind icon
```

## Usage

1. Enter a city name in the search box
2. Click "Search" or press Enter
3. View the weather information for that city
4. Use the navigation to return to the home page

## Technologies Used

- **Backend:** Python Flask
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Weather API:** Weather by API Ninjas (via RapidAPI)
- **Icons:** Font Awesome

## Notes

- The app uses the Weather by API Ninjas service through RapidAPI
- Make sure you have an active internet connection to fetch weather data
- The API key is included in the code for demonstration purposes 