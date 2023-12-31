import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => console.log('Redis client connected on the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

const cities = {
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
}

for (const city in cities) {
  client.hset('HolbertonSchools', city, cities[city], redis.print);
}

client.hgetall('HolbertonSchools', (err, value) => {
  console.log(value);
});
