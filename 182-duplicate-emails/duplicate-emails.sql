# Write your MySQL query statement below
SELECT email AS Email
FROM Person
GROUP BY email
HAVING count(id)>1