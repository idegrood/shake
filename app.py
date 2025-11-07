from flask import Flask, render_template, request, jsonify
import sys
sys.path.append('/home/pi/shake/shake_table')

app = Flask(__name__)

# not initialized
table = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_sine', methods=['POST'])
def run_sine():
    data = request.json
    amplitude = int(data.get('amplitude', 250))
    frequency = float(data.get('frequency', 5.0))
    duration = float(data.get('duration', 3.0))
    
    return jsonify({'status': 'success', 'amplitude': amplitude, 'frequency': frequency, 'duration': duration})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
