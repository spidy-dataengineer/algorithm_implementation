select w1.id
from weather w1
	join weather w2
   		on w1.recordDate = date_add(w2.recordDate, INTERVAL 1 DAY)
where w1.temperature > w2.temperature;

select id
from weather w1
where temperature > (
		select temperature
        from weather w2
        where w2.recordDate = date_sub(w1.recordDate, interval 1 day
);