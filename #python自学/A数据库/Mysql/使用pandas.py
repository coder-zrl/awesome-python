import pandas as pd
from sqlalchemy import create_engine

df=pd.read_excel('data.xlsx')
#创建引擎，连接数据库
engine = create_engine('mysql+pymysql://root:422518@localhost/student?charset=utf8')
#创建student表格
df.to_sql('student', engine, index=False, if_exists='append')