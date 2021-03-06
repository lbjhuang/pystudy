from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root@localhost:3306/lottery')
#print(engine)
Base = declarative_base()    #生成sqlalchemy 的 orm基类

class Cqssc(Base):
    __tablename__ = "cqssc"
    id = Column(Integer, primary_key=True)
    open_number = Column(String(15))
    number = Column(String(10))
    total = Column(Integer)
    open_time = Column(String(30))
    spider_time = Column(String(30))


    def insertData(self, data):
        Session_class = sessionmaker(bind=engine)
        Session = Session_class()  # 生成session实例
        data_obj = Cqssc(open_number = data.get('open_number'), number = data.get('number'),  total = data.get('total'), open_time= data.get('open_time'), spider_time = data.get('spider_time'))
        Session.add(data_obj)
        Session.commit()

# data = {'open_number': '20180411064', 'number': '0,0,7,7,1', 'open_time': '2018-04-11 16:41', 'spider_time': '2018-04-11 16:43:55'}
# cq = Cqssc()
# cq.insertData(data)