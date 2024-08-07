from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Use a global variable for simplicity. In a real-world app, you'd use a database.
count = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/count', methods=['GET'])
def get_count():
    global count
    count += 1
    return jsonify({"count": count})

if __name__ == '__main__':
    # This is only used for local development
    app.run(debug=True)