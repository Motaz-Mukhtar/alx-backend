import redis from 'redis';
const = { promisify } = require('util');

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => console.log('Redis client connected on the server'));

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue (schoolName) {
  console.log(await getAsync(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', 100);
displaySchoolValue('HolbertonSanFrancisco');
