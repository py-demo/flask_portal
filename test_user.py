#coding=utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, MetaData, Integer, String, DATETIME
from sqlalchemy import Sequence
from sqlalchemy.sql import text
import ConfigParser
import uuid
import datetime
import demjson

eis = dict()

class UserAction:
    def __init__(self):
        self.config_action()

        pass

    def config_action(self):
        # 读取配置文件中连接字符串
        config = ConfigParser.RawConfigParser()
        config.read("app.config")

        connectionstring = config.get("Connection1", "datasource")
        eis["connectionstring"] = connectionstring

        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.db = self.engine.connect()

        self.metadata = MetaData()

        self.user_table = Table(
            'eis_user',
            self.metadata,
            Column('USERNAME_', String),
            Column('PASSWORD_', String),
            Column('CNAME_', String),
            Column('ENAME_', String),
            Column('IS_ADMIN_', Integer),
            Column('COMPANY_ID_', String),
            Column('ENABLED_', Integer)
        )

        self.metadata.create_all(self.engine)

        pass

    def add_user(self):


        pass

    def select_all_user(self):
        sql = text('select * from eis_user')

        rows = self.db.execute(sql).fetchall()

        for row in rows:
            temp = row

        print rows

        dbo = self.db

        md = self.metadata

        print "s"

        s = "select * from eis_user WHERE USERNAME_ = '" + 'SQ.Li' + "'"

        a = "select * from eis_user where USERNAME_ = '%s'"

        pass

    def select_user(self):


        s1 = ("select * from eis_user WHERE USERNAME_ =  '%s'" % ('SQ.Li'))
        #s2 = (a % ('SQ.Li'))

        sql = text(s1)

        rows1 = self.db.execute(sql).fetchall()

        row_0 = rows1[0]

        pass

class RoleAction:
    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read("app.config")

        connectionstring = config.get("Connection", "datasource")
        eis["connectionstring"] = connectionstring

        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        self.user_table = Table(
            'eis_role',
            self.metadata,
            Column('ID_', String),
            Column('COMPANY_ID_', String),
            Column('NAME_', String),
            Column('DEPT_ID_', String),
            Column('CREATE_DATE_', DATETIME),
            Column('DESC_', String)
        )

        self.metadata.create_all(self.engine)

        pass

    def func1(self):
        try:
            id = str(uuid.uuid1()).replace('-', '')
            id = id.encode("UTF-8")
            tid = str(uuid.uuid1()).replace('-', '')
            tid = id.encode("UTF-8")
            name = u'总裁'
            dept = str(uuid.uuid1()).replace('-', '')
            dept = dept.encode("UTF-8")
            desc = u'赵钱孙李周吴郑王'
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            dt = dt.encode("UTF-8")

            sql_str = "insert into eis_role(ID_, COMPANY_ID_, NAME_, DEPT_ID_, DESC_, CREATE_DATE_) VALUE('%s', '%s', '%s', '%s', '%s', '%s')" % (id, tid, name, dept, desc, dt)

            sql = text(sql_str)

            self.dbo.execute(sql)

            pass
        except Exception, ex:
            print ex.message

            pass
        finally:

            pass


        pass

    def func2(self):

        sql_str = "select * from eis_role"

        sql = text(sql_str)

        rows = self.dbo.execute(sql)

        for row in rows:
            dt = row["CREATE_DATE_"]
            id = row["ID_"]

        data_json = demjson.encode(rows)


        print data_json

        pass


if __name__ == "__main__":
#    ua = UserAction()
#    ua.add_user()

#    ua.select_user()

    ra = RoleAction()
    ra.func1()
    ra.func2()

    print 'AAAA'

#    pass