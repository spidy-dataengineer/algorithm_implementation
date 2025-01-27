SELECT A.ANIMAL_ID,
       A.ANIMAL_TYPE,
       A.NAME
FROM (
      SELECT *
      FROM ANIMAL_INS -- 동물 보호소에 들어온 정보
      WHERE SEX_UPON_INTAKE IN ('Intact MALE', 'Intact Female')
     ) A
INNER JOIN (
            SELECT *
            FROM ANIMAL_OUTS -- 동물 보호소에서 입양 보낸 동물의 정보
            WHERE SEX_UPON_OUTCOME IN ('Neutered Male', 'Spayed Female')
           ) B
ON A.ANIMAL_ID = B.ANIMAL_ID