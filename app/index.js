// app/index.js
const http = require('http');
const os = require('os');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.write(`Hello from ${os.hostname()}\n`);
    res.end();
});

server.listen(3000, () => {
    console.log('Server is running on port 3000');
});
