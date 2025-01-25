const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const response = ['This is the list of our students'];
      await countStudents(process.argv[2])
        .then((data) => {
          Object.entries(data).forEach(([field, fieldData]) => {
            response.push(`Number of students in ${field}: ${fieldData.count}. List: ${fieldData.names.join(', ')}`);
          });
        });
      res.end(response.join('\n'));
    } catch (error) {
      res.end('This is the list of our students\nCannot load the database');
    }
  }
});

app.listen(1245);

module.exports = app;
