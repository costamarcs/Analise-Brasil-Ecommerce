#%%
import pandas as pd
from sqlalchemy import create_engine

usuario = 'postgres'
senha = 'marco123'
host = 'localhost'
porta = '5432'
banco = 'Brasil_olist'


engine = create_engine(f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco}')

query = ("""
    select *
    from public.olist_orders_dataset as OrdDt
    left join public.olist_order_reviews_dataset as OrdRvw 
         on OrdDt.order_id = OrdRvw.order_id
    left join public.olist_order_items_dataset as OrdItms 
         on OrdDt.order_id = OrdItms.order_id
    where OrdRvw.review_id is not null 
    limit 100
""")

df = pd.read_sql(query, engine)

print(df.head())
#%%
df