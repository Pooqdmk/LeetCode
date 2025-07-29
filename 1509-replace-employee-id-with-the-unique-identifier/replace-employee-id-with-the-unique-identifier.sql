# Write your MySQL query statement below
select e.unique_id ,s.name
from Employees s
left join EmployeeUNI e on e.id = s.id