select column_name as property, 
       upper(column_name) as label 
from information_schema.columns 
where table_name = 'order'
order by 1