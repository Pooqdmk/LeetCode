# Write your MySQL query statement below
select name from SalesPerson
where sales_id not in (select o.sales_id from Orders o join Company c on c.com_id = o.com_id where c.name = 'RED')