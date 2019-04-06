select *
from public.order
where id in :ids
and date between :date_min and :date_max