import pandas as pd
from sqlalchemy import create_engine

df=pd.read_excel('data.xlsx')
#�������棬�������ݿ�
engine = create_engine('mysql+pymysql://root:422518@localhost/student?charset=utf8')
#����student���
df.to_sql('student', engine, index=False, if_exists='append')