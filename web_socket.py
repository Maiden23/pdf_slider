from flask import Flask, render_template
from flask_socketio import SocketIO
from string import ascii_letters
app = Flask(__name__, template_folder="template")
socketio = SocketIO(app, async_mode="eventlet")

@app.route("/", methods=["GET","POST"])
def home():
    return render_template("index.html")

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

@socketio.on('change_slide')
def handle_change_slide(data):
    slide_number = data.get("slide")
    socketio.emit("update_slide", {"slide": slide_number})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=3030, debug=True)
