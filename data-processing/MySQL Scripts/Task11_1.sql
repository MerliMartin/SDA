# List the names of all customers and their booking costs greater than 1000
SELECT clients.name AS customer_name, bookings.total_amount AS booking_cost
FROM clients
INNER JOIN bookings ON clients.client_id=bookings.client_id
WHERE bookings.total_amount > 1000;