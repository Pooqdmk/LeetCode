# Write your MySQL query statement below
select name, case when sum(distance) is not null then sum(distance) else 0 end as travelled_distance
from Users u
left join Rides r
on u.id = r.user_id
group by user_id
order by travelled_distance desc,name 