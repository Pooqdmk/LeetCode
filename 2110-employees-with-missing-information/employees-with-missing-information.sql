# Write your MySQL query statement below
select e.employee_id
from Employees e
left join Salaries s on e.employee_id = s.employee_id
where e.name is null or s.salary is null

union
select s.employee_id
from Employees e
right join Salaries s on e.employee_id = s.employee_id
where e.name is null or s.salary is null

order by employee_id

