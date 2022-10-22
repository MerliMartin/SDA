# 2. List all reservations with a total cost in the range of 1000-2555.
SELECT *
FROM bookings
WHERE total_amount BETWEEN 1000 and 2555