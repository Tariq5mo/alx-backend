import { createClient } from 'redis';
import express from 'express';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const app = express();
const port = 1245;
const reservationKey = 'available_seats';

client.set(reservationKey, 50);

app.get('/available_seats', (req, res) => {
  client.get(reservationKey, (err, seats) => {
    res.json({ numberOfAvailableSeats: seats });
  });
});

app.get('/reserve_seat', (req, res) => {
  client.decr(reservationKey, (err, seats) => {
    if (seats < 0) {
      client.incr(reservationKey);
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation confirmed' });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
