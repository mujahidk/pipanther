from app import app

# Load configuration from config.py
app.config.from_object('config')

# Start web server
app.run(host='0.0.0.0', port=9000)
