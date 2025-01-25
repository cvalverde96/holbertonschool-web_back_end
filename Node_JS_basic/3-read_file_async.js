const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const fileContent = await fs.readFile(path, 'utf-8');
    const lines = fileContent.trim().split('\n');
    const students = lines.sclice(1).filter((line) => line.length > 0);

    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = { count: 0, names: [] };
      }
      fields[field].count += 1;
      fields[field].names.push(firstname);
    });

    Object.entries(fields).forEach(([field, data]) => {
      const nameList = data.names.join(', ');
      console.log(`Number of students in ${field}: ${data.count}. List: ${nameList}`);
    });
    return fields;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
