# coding:utf8

from sqlalchemy import create_engine, Table, Column, Integer, String, \
    Sequence, ForeignKey, MetaData, DATETIME

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, base
from sqlalchemy.sql import text

# 创建数据库引擎
engine = create_engine("mysql+pymysql://root:root@localhost/py_db", encoding="utf-8", echo=True)

# 创建会话连接、绑定据库引擎
Session = sessionmaker(bind=engine)

# 接下来session就能进行数据操作了
session = Session()

# 创建基础类
BaseModel = declarative_base()

metadata = MetaData()


# 创建用户类型
class User(BaseModel):
    __tabelname__ = "eis_user"
    id_ = Column(Integer, primary_key=True)
    cname_ = Column(String(255), unique=True)
    ename_ = Column(String(255), unique=True)
    password_ = Column(String(255), unique=True)
    is_admin_ = Column(Integer, unique=True)
    company_id_ = Column(String(255), unique=True)
    enabled_ = Column(Integer, unique=True)


if __name__ == "__main__":
    metadata.create_all()
