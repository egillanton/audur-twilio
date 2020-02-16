from flask import Flask, request, render_template, jsonify
from argparse import ArgumentParser
from twilio.rest import Client
import os

# Init Flask App
app = Flask(__name__)
app.secret_key = os.urandom(12)  # Generic key for dev purposes only

# Setup Enviroment Varibles on your system before hands.
account_sid = 'AC573d29e7bf9ada9feb441529afd99b8c'
auth_token = 'a4378515b4e2f6ebe3591835e26fc860'

# Set your Twillo Phone Number Here:
twilio_phone = '+12018905734'

# Setup Twilio Client
client = Client(account_sid, auth_token)

# ======== Routing =========================================================== #
# -------- Home ---------------------------------------------------------- #
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# -------- DEMO ---------------------------------------------------------- #
@app.route('/demo', methods=['GET'])
def demo():
    return render_template('demo.html')
# -------- Send ---------------------------------------------------------- #
@app.route('/send', methods=['POST'])
def ask():
    message = request.json['message']
    phone_number = request.json['phone_number']

    response = client.messages \
        .create(body=message,
                from_=twilio_phone,
                to=phone_number
                )

    return jsonify(
        response=response.sid,
    )


# ======== Main ============================================================== #
if __name__ == '__main__':
    parser = ArgumentParser(description='Example Flask Application')
    parser.add_argument("-p", "--port", type=int,
                        metavar="PORT", dest="port", default=5000, help='Port number')
    parser.add_argument("--host", type=str, metavar="HOST",
                        dest="host", default="localhost")
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=True)
