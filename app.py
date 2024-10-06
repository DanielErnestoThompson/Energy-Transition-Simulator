from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    # Get the request data (the inputs sent from the frontend)
    data = request.get_json()

    # Extract inputs from the request
    carbon_price = data.get('carbon_price')
    subsidies = data.get('subsidies')

    # For now, let's simulate by just returning the inputs (you can add real simulation logic here)
    result = {
        "carbon_price_received": carbon_price,
        "subsidies_received": subsidies,
        "simulation_output": "Simulation logic goes here!"
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
