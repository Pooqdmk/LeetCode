# Write your MySQL query statement below
-- select player_id,min(event_date) as first_login
-- from activity
-- group by player_id
-- order by player_id

with cte as(
    select player_id,event_date,row_number() over(partition by player_id order by event_date) as rn
    from activity
)
select player_id,event_date as first_login
from cte
where rn=1
order by player_id

