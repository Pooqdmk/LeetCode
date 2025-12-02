select d.name as Department,e.name as Employee,salary
from Employee e
join Department d
on e.departmentId = d.id
where (d.name,salary) in (
    select d.name as Department,max(salary) as salary
    from Employee e
    join Department d
    on e.departmentId = d.id
    group by d.id
)
