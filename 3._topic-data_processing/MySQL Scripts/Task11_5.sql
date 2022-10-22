/* 5. * List:
a. average amount of money spent by each customer - column naming: 
Average_reservations_price
b. the number of rented cars for each customer, taking into account only those 
customers who have rented at least two cars - column nomenclature: Number of 
rented cars
c. name and surname of the client - nomenclature of the columns: Name, Surname
d. sorting by the largest number of rental cars. All with one query.
*/
select avg(bookings.total_amount) as Average_reservations_price,
count(bookings.car_id) as Number_of_rented_cars,
clients.name as Name,
clients.surname as Surname
from bookings
inner join clients on clients.client_id = bookings.client_id
group by bookings.client_id
having Number_of_rented_cars >= 2
order by Number_of_rented_cars desc;