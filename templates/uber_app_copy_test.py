from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

rides = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/request_ride', methods=['POST'])
def request_ride():
    data = request.get_json()
    user_id = data.get('user_id')
    origin = data.get('origin')
    destination = data.get('destination')

    ride = {
        'user_id': user_id,
        'origin': origin,
        'destination': destination,
        'status': 'Requested'
    }

    rides.append(ride)

    return jsonify({'message': 'Ride requested successfully!'})

@app.route('/api/get_rides', methods=['GET'])
def get_rides():
    return jsonify({'rides': rides})

if __name__ == '__main__':
    app.run(debug=True)
