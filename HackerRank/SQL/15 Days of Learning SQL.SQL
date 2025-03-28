SELECT Total_Count.submission_date
        , Total_Count.total_number_of_unique_hackers
        , Max_Value.hacker_id
        , H.name
FROM
    (SELECT T.submission_date
           ,COUNT(1) AS total_number_of_unique_hackers
       FROM
            (SELECT submission_date
                   ,hacker_id
                   ,ROW_NUMBER() OVER(PARTITION BY hacker_id ORDER BY submission_date)
                    - (submission_date - to_date('2016-03-01', 'YYYY-MM-DD')) AS cmp
              FROM (SELECT submission_date, hacker_id
                    FROM Submissions
                GROUP BY submission_date, hacker_id)
            ORDER BY hacker_id) T
       WHERE T.cmp = 1
    GROUP BY T.submission_date) Total_Count
    ,
    (SELECT T.submission_date
           ,T.hacker_id
           ,ROW_NUMBER() OVER(PARTITION BY T.submission_date ORDER BY CNT DESC) AS IDX
    FROM (SELECT S.submission_date
                   , S.hacker_id
                   , COUNT(1) CNT
            FROM Submissions S
         GROUP BY S.submission_date, S.hacker_id
         ORDER BY S.submission_date, CNT DESC, S.hacker_id) T) Max_Value
    , hackers H
WHERE Total_Count.submission_date = Max_Value.submission_date
   AND Max_Value.hacker_id = H.hacker_id
   AND Max_Value.IDX = 1
;