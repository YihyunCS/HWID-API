from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# store registered HWIDs with their expiration times
registered_hwids = {}

@app.route('/register', methods=['POST'])
def register_hwid():
    data = request.get_json()
    hwid = data.get('hwid')
    software_id = data.get('softwareId')
    duration = data.get('duration')  # duration in days

    if not hwid or not software_id or not duration:
        return jsonify({'message': 'HWID, Software ID, and Duration are required.'}), 400

    expiry_time = datetime.now() + timedelta(days=int(duration))

    if software_id not in registered_hwids:
        registered_hwids[software_id] = []

    registered_hwids[software_id].append({
        'hwid': hwid,
        'expiry_time': expiry_time
    })
    return jsonify({'message': 'HWID registered successfully.'}), 200

@app.route('/verify', methods=['POST'])
def verify_hwid():
    data = request.get_json()
    hwid = data.get('hwid')
    software_id = data.get('softwareId')

    if not hwid or not software_id:
        return jsonify({'message': 'HWID and Software ID are required.'}), 400

    if software_id in registered_hwids:
        for record in registered_hwids[software_id]:
            if record['hwid'] == hwid:
                if datetime.now() <= record['expiry_time']:
                    return jsonify({'message': 'HWID verified successfully.'}), 200
                else:
                    return jsonify({'message': 'HWID has expired.'}), 403
    return jsonify({'message': 'HWID not found.'}), 403

@app.route('/list', methods=['GET'])
def list_hwids():
    response = []
    for software_id, hwid_list in registered_hwids.items():
        response.append({
            "softwareId": software_id,
            "hwids": [
                {
                    "hwid": hwid_data['hwid'],
                    "expiry_time": hwid_data['expiry_time'].strftime("%Y-%m-%d %H:%M:%S")
                }
                for hwid_data in hwid_list
            ]
        })
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
