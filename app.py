from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store registered HWIDs
registered_hwids = {}

@app.route('/register', methods=['POST'])
def register_hwid():
    data = request.get_json()
    hwid = data.get('hwid')
    software_id = data.get('softwareId')

    if not hwid or not software_id:
        return jsonify({'message': 'HWID and Software ID are required.'}), 400

    if software_id not in registered_hwids:
        registered_hwids[software_id] = []

    registered_hwids[software_id].append(hwid)
    return jsonify({'message': 'HWID registered successfully.'}), 200

@app.route('/verify', methods=['POST'])
def verify_hwid():
    data = request.get_json()
    hwid = data.get('hwid')
    software_id = data.get('softwareId')

    if not hwid or not software_id:
        return jsonify({'message': 'HWID and Software ID are required.'}), 400

    if software_id in registered_hwids and hwid in registered_hwids[software_id]:
        return jsonify({'message': 'HWID verified successfully.'}), 200
    else:
        return jsonify({'message': 'HWID not found.'}), 403

@app.route('/list', methods=['GET'])
def list_hwids():
    response = []
    for software_id, hwids in registered_hwids.items():
        response.append({
            "softwareId": software_id,
            "hwids": hwids
        })
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
