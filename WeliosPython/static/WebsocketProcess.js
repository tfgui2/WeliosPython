var sock = io({ transports: ['websocket'], rememberTransport: false });

sock.on('connect', function () {
    sock.send('new_connect');
});

function sendClick(msg) {
    sock.send(msg);
    console.log(msg);
}