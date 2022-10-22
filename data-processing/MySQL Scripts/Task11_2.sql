/*2. List the city of residence of all customers who rented a car in the period 12-20.07.2020, 
and the engine power of the rental car is not more than 120, sorting by the highestrental 
cost */
SELECT clients.city AS clients_city, bookings.total_amount AS booking_amount
FROM clients
INNER JOIN bookings ON clients.client_id = bookings.client_id
INNER JOIN cars ON cars.car_id = bookings.car_id
WHERE bookings.start_date >= '2020-07-12'
AND bookings.end_date <= '2020-07-20'
AND cars.horse_power <= 120
ORDER BY bookings.total_amount DESC;
