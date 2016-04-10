# Create log directory
mkdir -p log

# Start the Flask server in background, redirect output to log directory.
python src/run.py >> log/access.log 2>&1 &
