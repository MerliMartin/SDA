# 4. List the sum of the costs of all bookings that were made in the period July 14-18, 2020
select sum(total_amount) as period_sum 
from bookings
where start_date >= '2020-07-14'
and end_date <= '2020-07-18'
;