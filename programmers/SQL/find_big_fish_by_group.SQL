-- https://school.programmers.co.kr/learn/courses/30/lessons/293261
WITH JOINED_TB AS(
    SELECT A.ID,
           A.FISH_TYPE,
           COALESCE(A.LENGTH,10) AS LENGTH,
           B.FISH_NAME,
           ROW_NUMBER() OVER(PARTITION BY A.FISH_TYPE ORDER BY A.LENGTH DESC) AS RN_DESC
    FROM FISH_INFO A
    INNER JOIN FISH_NAME_INFO B
    ON A.FISH_TYPE = B.FISH_TYPE
)
SELECT ID,
       FISH_NAME,
       LENGTH
FROM JOINED_TB
WHERE RN_DESC = 1
ORDER BY ID;
------------------------------------------------------------------------------------------
-- JOIN, ON, 서브쿼리 사용
SELECT ID, FISH_NAME, A.LENGTH AS LENGTH
FROM FISH_INFO A
INNER JOIN FISH_NAME_INFO B
ON A.FISH_TYPE = B.FISH_TYPE
WHERE A.FISH_TYPE IN
(
    SELECT FISH_TYPE
    FROM FISH_INFO
    GROUP BY FISH_TYPE
    HAVING LENGTH = MAX(LENGTH)
)
ORDER BY ID

-- 1. 쿼리 동작 방식 비교
-- 첫 번째 쿼리 (ROW_NUMBER 사용):
-- ROW_NUMBER를 사용해 각 FISH_TYPE별로 길이가 가장 긴 물고기를 순위 매깁니다.
-- WHERE RN_DESC = 1 조건을 통해 각 물고기 종류의 최대 길이 하나만 추출합니다.
-- 윈도우 함수는 전체 데이터에 대해 한 번만 계산되므로, O(N log N) 수준의 성능을 가집니다.
-- 두 번째 쿼리 (서브쿼리 사용):
-- 서브쿼리에서 각 FISH_TYPE별로 MAX(LENGTH)를 구합니다.
-- 이후 메인 쿼리에서 다시 JOIN을 수행해 해당 길이를 가진 레코드를 찾습니다.
-- 이 방식은 서브쿼리에서 GROUP BY와 MAX 계산 후, 메인 쿼리에서 다시 JOIN을 수행하므로 데이터가 많을 경우 서브쿼리가 반복 실행될 수 있습니다.
-- 비효율적인 서브쿼리와 JOIN이 중첩되면서, **O(N^2)**에 가까운 성능이 나올 수 있습니다.
-- 2. 효율성 분석
-- 데이터량이 적을 경우: 두 쿼리 모두 비슷한 성능을 보일 수 있지만, 첫 번째 쿼리가 더 일관된 성능을 보입니다.
-- 데이터량이 많을 경우: 첫 번째 쿼리는 윈도우 함수가 인덱스를 사용할 수 있어 성능이 더 뛰어납니다. 반면, 두 번째 쿼리는 서브쿼리와 JOIN이 반복되므로 성능 저하가 발생할 수 있습니다.
-- 3. 인덱스 고려
-- 첫 번째 쿼리에서 FISH_INFO(FISH_TYPE, LENGTH)에 인덱스가 있다면 윈도우 함수의 정렬 작업이 빨라집니다.
-- 두 번째 쿼리에서는 FISH_INFO(FISH_TYPE, LENGTH)에 인덱스가 없으면 서브쿼리가 느려질 수 있습니다.
-- 결론
-- **첫 번째 쿼리 (ROW_NUMBER 사용)**이 더 효율적이고 유지보수하기 쉽습니다.
-- 서브쿼리 방식은 비효율적일 수 있으므로, 특별한 이유가 없다면 첫 번째 쿼리를 사용하는 것이 좋습니다.
-- 대규모 데이터에서는 윈도우 함수가 최적화에 유리하며, 인덱스를 적절히 설정하면 더욱 빠르게 동작합니다.
