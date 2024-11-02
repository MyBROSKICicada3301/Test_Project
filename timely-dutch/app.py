
# from flask import Flask, jsonify, render_template
# import threading
# import zmq

# # Flask app
# app = Flask(__name__)

# # Data structure to store incoming messages
# train_data = {
#     "arrivals": [],
#     "departures": [],
#     "services": []
# }

# # Configuration
# SOURCE_SERVER = "tcp://pubsub.besteffort.ndovloket.nl:7664"
# ARRIVALS_TOPIC = "/RIG/InfoPlusDASInterface4"
# DEPARTURES_TOPIC = "/RIG/InfoPlusDVSInterface4"
# SERVICES_TOPIC = "/RIG/InfoPlusRITInterface2"

# # Fetch train status
# def update_train_data():
#     context = zmq.Context()
#     socket = context.socket(zmq.SUB)
#     socket.connect(SOURCE_SERVER)
#     socket.setsockopt_string(zmq.SUBSCRIBE, ARRIVALS_TOPIC)
#     socket.setsockopt_string(zmq.SUBSCRIBE, DEPARTURES_TOPIC)
#     socket.setsockopt_string(zmq.SUBSCRIBE, SERVICES_TOPIC)

#     while True:
#         topic, message = socket.recv_multipart()
#         data = message.decode("utf-8")  # Assume JSON or parsable format

#         if topic.decode("utf-8") == ARRIVALS_TOPIC:
#             train_data["arrivals"] = data  # Update arrivals
#         elif topic.decode("utf-8") == DEPARTURES_TOPIC:
#             train_data["departures"] = data  # Update departures
#         elif topic.decode("utf-8") == SERVICES_TOPIC:
#             train_data["services"] = data  # Update services

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/api/train-status", methods=["GET"])
# def get_train_status():
#     return jsonify(train_data)

# # Run the data retrieval in a separate thread
# if __name__ == "__main__":
#     threading.Thread(target=update_train_data, daemon=True).start()
#     app.run(host="0.0.0.0", port=8080)


# app.py
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
