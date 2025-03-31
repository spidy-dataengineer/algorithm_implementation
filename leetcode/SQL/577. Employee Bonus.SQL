SELECT A.name,
       B.bonus
FROM Employee A
LEFT OUTER JOIN bonus B
ON A.empId = B.empId
WHERE b.bonus < 1000 or b.bonus IS NULL;