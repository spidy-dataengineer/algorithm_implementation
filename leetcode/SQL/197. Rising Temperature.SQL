select w1.id
from weather w1
	join weather w2
   		on w1.recordDate = date_add(w2.recordDate, INTERVAL 1 DAY) -- 테이블의 하루 다음날 꺼랑 조인을해야 선행 테이블이 다음날이고, 뒤에 테이블이 원래의 테이블값으로 나옴
where w1.temperature > w2.temperature;


select id
from weather w1
where temperature > (
		select temperature
        from weather w2
        where w2.recordDate = date_sub(w1.recordDate, interval 1 day
);