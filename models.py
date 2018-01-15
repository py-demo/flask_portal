# coding:utf8

from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接/创建数据库引擎
engine = create_engine("mysql://root:root@127.0.0.1:3306/py_db", encoding="utf-8", echo=True)

# 创建会话连接/绑定据库引擎
Session = sessionmaker(bind=engine)
session = Session()

# 创建基础类
Base = declarative_base()


# 创建用户类型
class User(Base):
    __tablename__ = 'eis_user'
    id_ = Column(Integer, primary_key=True)
    cname_ = Column(String(255), unique=True)
    ename_ = Column(String(255), unique=True)
    password_ = Column(String(255), unique=True)
    is_admin_ = Column(Integer, unique=True)
    company_id_ = Column(String(255), unique=True)
    enabled_ = Column(Integer, unique=True)

    def __repr__(self):
        return "<User(cname_='%s',ename_='%s',password_='%s')>" % (self.cname_,self.ename_,self.password_)


User.metadata.create_all(engine)

new_user = User(
    id_=2,
    cname_='张三',
    ename_='zhangSan',
    password_='123456',
    is_admin_=1,
    company_id_='1001',
    enabled_=1
)

# session.add(new_user)
# session.commit()

rows = session.execute('select * from eis_user').fetchall()
row = session.execute("select * from eis_user where ename_='zhangSan'").first()

print row
for row in rows:
    # print row
    pass

# all = session.query(User).all()
row = session.query(User).filter(User.ename_ == 'zhangSan').one()

print row
# print all
