from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
from datetime import datetime, timedelta

app = Flask(__name__)

import random
from datetime import datetime, timedelta

def get_weather_data(city):
    """Generate mock weather data for demonstration"""
    # Generate realistic weather data based on city name
    city_lower = city.lower()
    
    # Base temperatures for different regions
    if any(region in city_lower for region in ['delhi', 'mumbai', 'chennai', 'kolkata', 'bangalore', 'india']):
        base_temp = 30
        humidity_range = (60, 80)
    elif any(region in city_lower for region in ['london', 'paris', 'berlin', 'rome', 'madrid', 'europe']):
        base_temp = 15
        humidity_range = (70, 85)
    elif any(region in city_lower for region in ['new york', 'los angeles', 'chicago', 'miami', 'usa', 'america']):
        base_temp = 20
        humidity_range = (50, 70)
    elif any(region in city_lower for region in ['tokyo', 'beijing', 'seoul', 'shanghai', 'asia']):
        base_temp = 25
        humidity_range = (65, 75)
    else:
        base_temp = 22
        humidity_range = (60, 75)
    
    # Generate random variations
    temp_variation = random.uniform(-5, 5)
    current_temp = base_temp + temp_variation
    
    # Calculate sunrise and sunset times (approximate)
    now = datetime.now()
    sunrise_time = now.replace(hour=6, minute=30, second=0, microsecond=0)
    sunset_time = now.replace(hour=18, minute=30, second=0, microsecond=0)
    
    weather_data = {
        'temp': round(current_temp, 1),
        'feels_like': round(current_temp + random.uniform(-2, 2), 1),
        'min_temp': round(current_temp - random.uniform(3, 8), 1),
        'max_temp': round(current_temp + random.uniform(3, 8), 1),
        'humidity': random.randint(*humidity_range),
        'wind_speed': round(random.uniform(5, 25), 1),
        'wind_degrees': random.randint(0, 360),
        'sunrise': int(sunrise_time.timestamp()),
        'sunset': int(sunset_time.timestamp())
    }
    
    return weather_data

@app.route('/')
def index():
    """Main page route"""
    return render_template('index.html')

@app.route('/api/weather/<city>')
def weather_api(city):
    """API endpoint to get weather data for a city"""
    weather_data = get_weather_data(city)
    
    if weather_data:
        # Convert sunrise and sunset timestamps to readable format
        if 'sunrise' in weather_data:
            weather_data['sunrise_formatted'] = datetime.fromtimestamp(
                weather_data['sunrise']).strftime('%H:%M:%S')
        if 'sunset' in weather_data:
            weather_data['sunset_formatted'] = datetime.fromtimestamp(
                weather_data['sunset']).strftime('%H:%M:%S')
        
        return jsonify({
            'success': True,
            'data': weather_data
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Failed to fetch weather data'
        }), 500

@app.route('/weather/<city>')
def weather_page(city):
    """Route to display weather for a specific city"""
    weather_data = get_weather_data(city)
    
    if weather_data:
        # Convert timestamps
        if 'sunrise' in weather_data:
            weather_data['sunrise_formatted'] = datetime.fromtimestamp(
                weather_data['sunrise']).strftime('%H:%M:%S')
        if 'sunset' in weather_data:
            weather_data['sunset_formatted'] = datetime.fromtimestamp(
                weather_data['sunset']).strftime('%H:%M:%S')
        
        return render_template('weather.html', city=city, weather=weather_data)
    else:
        return render_template('error.html', city=city)

@app.route('/search', methods=['GET'])
def search():
    """Handle search form submission"""
    city = request.args.get('city', '').strip()
    if city:
        return redirect(url_for('weather_page', city=city))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 