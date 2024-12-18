WITH RECURSIVE GenerationCTE AS (
    -- 초기 세대: PARENT_ID가 NULL인 경우
    SELECT
        ID,
        PARENT_ID,
        1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL

    UNION ALL

    -- 재귀적으로 자식 개체의 세대 계산
    SELECT
        e.ID,
        e.PARENT_ID,
        g.GENERATION + 1 AS GENERATION
    FROM ECOLI_DATA e
    INNER JOIN GenerationCTE g ON e.PARENT_ID = g.ID
),
-- 각 개체의 자식 수 계산
ChildCountCTE AS (
    SELECT
        p.ID,
        COUNT(c.ID) AS CHILD_COUNT
    FROM ECOLI_DATA p
    LEFT JOIN ECOLI_DATA c ON p.ID = c.PARENT_ID
    GROUP BY p.ID
)
-- 세대별 자식이 없는 개체 수 계산
SELECT COUNT(*) AS COUNT,
    g.GENERATION
FROM GenerationCTE g
INNER JOIN ChildCountCTE c ON g.ID = c.ID
WHERE c.CHILD_COUNT = 0
GROUP BY g.GENERATION
ORDER BY g.GENERATION;
