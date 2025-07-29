# Write your MySQL query statement below
-- with cte as(
-- select event_date
-- from Activity
-- group by player_id
-- order by event_date
-- limit 1
-- )

-- select distinct a.player_id,c.event_date
-- from activity a,cte c
-- order by a.player_id
select player_id,min(event_date) as first_login
from activity
group by player_id
order by player_id
-- order by player_id,event_date
