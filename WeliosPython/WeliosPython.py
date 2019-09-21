from flask import Flask, request, render_template
from flask_socketio import SocketIO, send
import ctypes

# 받은 메시지를 autoit으로 보내는 부분
autoit = ctypes.WinDLL("autoitx3_x64")
SendAuto = autoit ['AU3_Send']

# 웹소켓으로 클라에서 메시지를 받는 부분
app = Flask(__name__)
app.secret_key = "mysecret"
socket_io = SocketIO(app)

@app.route('/mfd')
def mfd():
    return render_template('mfd.html')

@socket_io.on('message')
def request(message):
    if message != 'new_connect':
        SendAuto(message)
        print(message)

if __name__ == '__main__':
    #app.run()
    socket_io.run(app, host='0.0.0.0', port=5000)

