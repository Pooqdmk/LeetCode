with cte as
(
select d.id as id,d.name as name,max(salary) as max_salary
from Employee e
join Department d
on e.departmentId = d.id
group by d.id
)
select cte.name as Department, e.name as Employee,e.salary as Salary 
from cte
join Employee e
on cte.id = e.departmentId and e.salary = max_salary