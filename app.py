from flask import Flask, jsonify, render_template
import threading
import time

app = Flask(__name__)

# Global variable to store the count
count = 0

def increment_count():
    global count
    while True:
        time.sleep(1)
        global count
        count += 1
        print(f"Count incremented: {count}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/count', methods=['GET'])
def get_count():
    return jsonify({"count": count})

if __name__ == '__main__':
    # Start the background thread to increment the count
    counter_thread = threading.Thread(target=increment_count)
    counter_thread.daemon = True
    counter_thread.start()

    # Run the Flask app
    app.run(debug=True)