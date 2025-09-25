SELECT p.product_id, p.product_name
FROM Product p
where exists (
    SELECT 1
    FROM Sales s
    WHERE s.product_id = p.product_id
)
and not exists (
    select 1
    from Sales s
    where s.product_id = p.product_id
    and (sale_date < '2019-01-01' or sale_date > '2019-03-31' )
)