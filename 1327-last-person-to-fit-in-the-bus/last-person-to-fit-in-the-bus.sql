with cte as
(
    select turn,person_name,
    sum(weight) over(order by turn) as tot_weight
    from Queue
    
)

select person_name
from cte
where tot_weight <= 1000
order by turn desc
limit 1

-- select person_name
-- from cte2
-- where 
