# List the id of all customers whose last name starts with 'J' and first name ends with 'ew'.
SELECT *
FROM clients
WHERE surname LIKE 'J%' AND name LIKE '%ew'