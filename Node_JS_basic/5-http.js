const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databasePath = process.argv[2];
    let responseText = 'This is the list of our students\n';

    try {
      const data = await countStudents(databasePath);
      const studentCounts = Object.entries(data)
        .map(([field, fieldData]) => `Number of students in ${field}: ${fieldData.count}. List: ${fieldData.names.join(', ')}`).join('\n');
      responseText += studentCounts;
    } catch (error) {
      responseText += 'Cannot load the database';
    }

    res.end(responseText);
  }
});

app.listen(1245);

module.exports = app;
