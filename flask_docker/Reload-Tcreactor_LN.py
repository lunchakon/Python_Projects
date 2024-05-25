from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reload', methods=['POST'])
def reload():
    secret_code = request.form.get('secret')
    if secret_code == 'TC-reactor-reload-JP':
        url = 'http://172.30.2.107:8080/command/reload'
        payload = {'secret': secret_code}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return 'Reload command sent successfully!'

    elif secret_code == 'TC-reactor-reload-SG':
        url = 'http://172.26.34.52:8080/command/reload'
        payload = {'secret': secret_code}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return 'Reload command sent successfully!'

    elif secret_code == 'tc-bloombergpub-reload':
        url = 'http://172.26.36.225:8009/command/reload'
        payload = {'secret': secret_code}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        return 'Reload command sent successfully!'

    else:
        return 'Invalid secret-code'

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0',port=9000)



