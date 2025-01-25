const http = require('http');

const app = http.createServer((req, rest) => {
  rest.writeHead(200, { 'Content-Type': 'text/plain' });
  rest.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
