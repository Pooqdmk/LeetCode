# Write your MySQL query statement below

select w1.id
from Weather w1
join Weather w2 on datediff(w1.recordDate,w2.recordDate) = 1
where w2.temperature < w1.temperature

