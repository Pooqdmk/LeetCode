with cte as
(
select s.user_id, round(sum(case when action = 'confirmed' then 1 else 0 end)/count(c.action),2) as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id
)

select user_id, case when confirmation_rate is not null then confirmation_rate else 0 end as confirmation_rate
from cte