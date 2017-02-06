--part_a
SELECT count(*) FROM Frequency WHERE docid = '10398_txt_earn';

--part_b
SELECT count(term) FROM Frequency WHERE docid = '10398_txt_earn' AND count = 1;

--part_c
SELECT distinct count(term) FROM (SELECT term FROM Frequency WHERE docid = '10398_txt_earn' AND count = 1 UNION SELECT term FROM Frequency WHERE docid = '925_txt_trade' AND count = 1);

--part_d
SELECT count(distinct docid) FROM Frequency WHERE term = 'law' or term = 'legal';

--part_e
select count(*) from (select docid, sum(count)
from frequency
group by docid
having sum(count) > 300
)
;


--part_f

select count(*)
from (select distinct(docid)
from frequency
where term ='transactions'
and count>0

intersect

select distinct(docid)
from frequency
where term='world'
and count>0
)
;

--part_g
select output from (select sum(A.value * B.value) as output, A.row_num as arow, B.col_num as bcol from A join B where (A.col_num=B.row_num) group by A.row_num, B.col_num) where arow = 2 and bcol = 3;


--part_h

select sum(f1.count*f2.count)
from frequency f1 join frequency f2 on f1.term=f2.term
where f1.docid='10080_txt_crude' 
and f2.docid='17035_txt_earn'
;



--part_i

select docid, max(tot) from(
select f.docid, sum(f.count*q.count) as tot
from frequency f join
(SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count)q on f.term=q.term
where q.docid='q'
group by f.docid
)
;

