select d.name as Department, e.name as Employee,salary as Salary
from (
    select e.*,
    dense_rank() over(partition by departmentId  order by salary desc) as rnk
    from Employee e
) e
join Department d
on d.id = e.departmentId
where rnk <= 3