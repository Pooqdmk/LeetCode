select request_at as Day, round(sum(case when status like 'cancelled%' then 1 else 0 end)/count(*),2) as `Cancellation Rate`
from Trips as t
join Users as u1
on t.client_id  = u1.users_id
join Users as u2
on t.driver_id = u2.users_id
where u1.banned = 'No' and u2.banned = 'No' and 
request_at between "2013-10-01" and "2013-10-03"
group by request_at 