SELECT A.name as Employee
FROM Employee A
INNER JOIN Employee B
ON A.managerId = B.id
WHERE A.salary > B.salary;