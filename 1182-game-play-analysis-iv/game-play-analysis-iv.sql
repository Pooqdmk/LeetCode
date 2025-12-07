with cte as
(
    select player_id, event_date, rank() over(partition by player_id order by event_date) as rnk
    from Activity

),

cte2 as
(   
    select count(a1.player_id) as cnt
    from cte a1
    join cte a2
    on a1.player_id = a2.player_id and
    a1.rnk + 1 = a2.rnk and datediff(a1.event_date, a2.event_date) = -1
    where a1.rnk = 1 and a2.rnk = 2
)

select round(cnt/(select count(distinct player_id) from Activity),2) as fraction
from cte2


