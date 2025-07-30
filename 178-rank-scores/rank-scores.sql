# Write your MySQL query statement below
select score,dense_rank() over(order by score desc) as `rank`
from Scores
order by `rank`
-- select score
-- from Scores
-- group by score
-- order by score desc