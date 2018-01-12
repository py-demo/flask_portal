#coding=utf-8

import sqlalchemy
from sqlalchemy import create_engine,Table, Column, ForeignKey, MetaData, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.sql import text

import uuid
eis = dict()

#租户管理
class TenantManageObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        #表对象

        self.metadata.create_all(self.engine)

        pass

    def create(self, name, desc):
        tenantid = ''

        try:
            tid = str(uuid.uuid1()).replace("-", "")

            sql_str = ("insert into eis_company(ID_, NAME_, DESC_) VALUE('%s', '%s', '%s')" % (tid, name, desc))

            sql = text(sql_str)

            self.dbo.execute(sql)

            tenantid = tid

        except Exception, ex:
            tenantid = ''
            print ex.message

            pass
        finally:
            return tenantid

    def edit(self, tid, name, desc):
        result = 0

        try:
            sql_str = ("update eis_company SET ID_ = '%s', NAME_ = '%s', DESC_ = '%s' WHERE(ID_ = '%s')" % (tid, name, desc, tid))

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message

            result = 0
        finally:
            return result

    #当前采用物理删除，直接删除数据；
    #后续采用逻辑删除，更新删除状态，并记录删除时间等
    def delete(self, tid):
        result = 0

        try:
            sql_str = ("delete from eis_company WHERE (ID_ = '%s')" % (tid))

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message

            result = 0
        finally:
            return result

    #根据企业ID查询企业信息
    def select4id(self, tid):

        pass

    #根据企业名称产销企业信息
    def select4name(self, name):

        pass

    #获取所有企业信息
    def getinfo_all(self):

        pass

    #获取查询企业信息；
    #pagecount：第几页
    #range：每页大小
    def getinfo_page(self, pagecount, range):

        pass






#账户管理
class AccountManageObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

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

    def add_user(self, map):
        result = 0
        try:
            str = "insert into eis_user(USERNAME_, PASSWORD_, CNAME_, ENAME_, IS_ADMIN_, COMPANY_ID, ENABLED_) value('%s', '%s', '%s', '%s', %d, '%s', %d)" % (map[""])



            result = 1

        except Exception, ex:
            print ex.message
            result = 0

            pass
        finally:

            return result

    def edit_user(self, map):
        result = 0
        try:


            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

    def del_user(self, map):
        result = 0
        try:

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result