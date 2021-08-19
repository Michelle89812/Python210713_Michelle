select id as 期數, n1, n2, n3, n4, n5, n6, (n1+n2+n3+n4+n5+n6) as 合計
from lotto
where 合計 < 50


select count(*) as 出現次數
from lotto
where n1=2 or n2=2 or n3=2 or n4=2 or n5=2 or n6=2

