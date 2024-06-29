from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('settings.json', 'r') as f:
    settings = json.load(f)

@app.route('/settings/<page>/<setting_id>', methods=['POST'])
def update_setting(page, setting_id):
    if page in settings:
        page_settings = settings[page]
        for setting in page_settings:
            if setting['id'] == setting_id:
                data = request.json
                setting.update(data)

                with open('settings.json', 'w') as f:
                    json.dump(settings, f, indent=4)
                return jsonify(setting)
        return jsonify({"error": "Setting not found"}), 404
    else:
        return jsonify({"error": "Page not found"}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
