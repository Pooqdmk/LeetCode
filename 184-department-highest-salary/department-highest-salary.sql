with cte as
(
    select d.id as id,d.name as name, max(salary) as salary
    from Employee e
    join Department d
    on e.departmentId = d.id
    group by d.id
)

select cte.name as Department, e.name as Employee, e.salary
from cte 
join Employee e
on e.departmentId = cte.id
where e.salary = cte.salary