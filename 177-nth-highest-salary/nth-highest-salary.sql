CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE offset_val INT;
    SET offset_val = N - 1;
  RETURN (

      # Write your MySQL query statement below.
    
    select salary 
    from (select distinct salary from Employee order by salary desc) as t
    limit 1 offset offset_val

  );
END