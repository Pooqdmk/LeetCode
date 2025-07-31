# Write your MySQL query statement below
select employee_id,department_id
from Employee
where primary_flag='Y'

union 

select employee_id,min(department_id) as department_id
from Employee
where employee_id not in (select employee_id from Employee where primary_flag='Y')
group by employee_id