SELECT p.product_id, p.product_name
FROM Product p
JOIN Sales s ON p.product_id = s.product_id 
group by p.product_id
having min(sale_date) >= '2019-01-01'
and max(sale_date) <= '2019-03-31'