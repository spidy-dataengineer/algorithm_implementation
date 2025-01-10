-- 전체 대여 횟수가 5회 이상인 애들 중에서 월별 대여 횟수 구하기
with rental as(
    select car_id, month(start_date) month
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where start_date between '2022-08-01' and '2022-10-31'
)

SELECT month, car_id, count(*) as records
from rental
where car_id in (
    select car_id
    from rental
    group by car_id
    having count(*) >= 5)
group by month, car_id
order by month asc, car_id desc