SELECT A.name as Customers
FROM Customers A
LEFT OUTER JOIN Orders B
ON A.id = B.customerId
WHERE B.id is NULL;