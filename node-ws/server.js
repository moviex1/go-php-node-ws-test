const WebSocket = require('ws');

const port = 8080;
const wss = new WebSocket.Server({ port: port });

wss.on('connection', function connection(ws) {
  
  ws.on('message', function incoming(message) {
    
    // Echo the received message back to the client
    ws.send(`Echo: ${message}`);
  });

  ws.on('close', function close() {
  });

  // Send a welcome message to the connected client
  ws.send('Welcome to the WebSocket server!');
});

console.log(`WebSocket server is running on ws://localhost:${port}`);

