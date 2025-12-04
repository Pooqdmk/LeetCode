with cte as
(
select *, rank() over(partition by product_id order by change_date desc) as rn
from Products
where change_date <= '2019-08-16'
),

cte2 as
(
    select product_id, case when '2019-08-16' >= change_date then new_price else 10 end as price
    from cte
    where rn = 1
)

select product_id,10 as price
from Products
where product_id not in (select product_id from cte2)

union

select product_id, case when '2019-08-16' >= change_date then new_price else 10 end as price
    from cte
    where rn = 1





