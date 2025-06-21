# Write your MySQL query statement below
#scalar sub query returns a null if nothing is given out by hte inner sub query 
#with a single select it nothin is is given by the limit then it prints nothing

select
(
select *
from MyNumbers
group by num
having count(num) = 1
order by num desc
limit 1
) as num