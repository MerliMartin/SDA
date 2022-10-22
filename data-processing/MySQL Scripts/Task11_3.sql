/** List the number of rental cars with a daily rental cost of 300 or more by grouping cars 
by engine power, sorting by smallest.*/
select *
from bookings
inner join cars on bookings.car_id = cars.car_id
where cars.price_per_day >= 300
group by cars.horse_power
order by cars.horse_power;