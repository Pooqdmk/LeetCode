select p.product_id, case when sum(units) !=0 then round(sum(price*units)*1.0/sum(units),2) else 0 end as average_price
from Prices p
left join UnitsSold u
on p.product_id  = u.product_id 
and purchase_date >= start_date and purchase_date <= end_date
group by p.product_id 

