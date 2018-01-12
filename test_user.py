#coding=utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, MetaData, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.sql import text
import ConfigParser

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

#if __name__ == "__main__":
#    ua = UserAction()
#    ua.add_user()

#    ua.select_user()

#    pass