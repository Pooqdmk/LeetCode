select round(sum(tiv_2016),2) as tiv_2016
from Insurance
where concat(lat,lon) in (
    select concat(lat,lon) as loc from Insurance
    group by loc
    having count(*) = 1  
    ) 
and tiv_2015 in (
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*) > 1
)

