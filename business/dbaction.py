#coding=utf-8

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, ForeignKey, MetaData, Integer, String, DATETIME
from sqlalchemy import Sequence
from sqlalchemy.sql import text

import uuid
import datetime

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
            sql_str = "insert into eis_user(USERNAME_, PASSWORD_, CNAME_, ENAME_, IS_ADMIN_, COMPANY_ID_, ENABLED_) value('%s', '%s', '%s', '%s', %d, '%s', %d)" % (map["username"], map["password"], map["cname"], map["ename"], map["is_admin"], map["tenantid"], map["enable"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

    def edit_user(self, map):
        result = 0
        try:
            sql_str = "update eis_user set USERNAME_ = '%s', PASSWORD_ = '%s', CNAME_ = '%s', ENAME_ = '%s', IS_ADMIN_ = %d, COMPANY_ID_ = '%s', ENABLED_ = %d WHERE (USERNAME_ = '%s')" % (map["username"], map["password"], map["cname"], map["ename"], map["is_admin"], map["tenantid"], map["enable"], map["username"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

    def del_user(self, map):
        result = 0
        try:
            sql_str = "delete from eis_user WHERE USERNAME_ = '%s'" % (map["username"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result


#角色管理
class RoleManageObject:
    def __init__(self):
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

    def create(self, map):
        result = None

        #生成ID
        tmp_rid = str(uuid.uuid1()).replace('-', '')
        rid = tmp_rid.encode("UTF-8")

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            sql_str = "insert into eis_role(ID_, COMPANY_ID_, NAME_, DEPT_ID_, DESC_, CREATE_DATE_) VALUE('%s', '%s', '%s', '%s', '%s', '%s')" % (rid, map["company_id"], map["name"], map["dept_id"], map["desc"], dt)

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = rid
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

    def edit(self, map):
        result = 0

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            sql_str = "update eis_role set ID_ = '%s', COMPANY_ID_ = '%s', NAME_ = '%s', DEPT_ID_ = '%s', DESC_ = '%s', CREATE_DATE_ = '%s' WHERE ID_ = '%s'" % (map["role_id"], map["company_id"], map["name"], map["dept_id"], map["desc"], dt, map["role_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

    def delete(self, map):
        result = 0

        try:
            sql_str = "delete from eis_role WHERE ID_ = '%s'" % (map["role_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

        pass


#岗位管理
class PositionManageObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        self.user_table = Table(
            'eis_position',
            self.metadata,
            Column('ID_', String),
            Column('COMPANY_ID_', String),
            Column('NAME_', String),
            Column('CREATE_DATE_', DATETIME),
            Column('DESC_', String)
        )

        self.metadata.create_all(self.engine)
        pass

    def create(self, map):
        result = ''

        # 生成ID
        tmp_pid = str(uuid.uuid1()).replace('-', '')
        pid = tmp_pid.encode("UTF-8")

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            sql_str = "insert into eis_position(ID_, COMPANY_ID_, NAME_, DESC_, CREATE_DATE_) VALUE('%s', '%s', '%s', '%s', '%s')" % (pid, map["company_id"], map["name"], map["desc"], dt)

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = pid
        except Exception, ex:
            print ex.message
            result = ''
        finally:
            return result

    def edit(self, map):
        result = 0

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            sql_str = "update eis_position set ID_ = '%s', COMPANY_ID_ = '%s', NAME_ = '%s', DESC_ = '%s', CREATE_DATE_ = '%s' WHERE ID_ = '%s'" % (map["position_id"], map["company_id"], map["name"], map["desc"], dt, map["position_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

        pass

    def delete(self, map):
        result = 0

        try:
            sql_str = "delete from eis_position WHERE ID_ = '%s'" % (map["position_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

        pass


#群组管理
class GroupManageObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        self.user_table = Table(
            'eis_group',
            self.metadata,
            Column('ID_', String),
            Column('COMPANY_ID_', String),
            Column('NAME_', String),
            Column('CREATE_DATE_', DATETIME),
            Column('DESC_', String)
        )

        self.metadata.create_all(self.engine)
        pass

    def create(self, map):
        result = ''

        # 生成ID
        tmp_gid = str(uuid.uuid1()).replace('-', '')
        gid = tmp_gid.encode("UTF-8")

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            sql_str = "insert into eis_group(ID_, COMPANY_ID_, NAME_, DESC_, CREATE_DATE_) VALUE('%s', '%s', '%s', '%s', '%s')" % (gid, map["company_id"], map["name"], map["desc"], dt)

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = gid
        except Exception, ex:
            print ex.message
            result = ''
        finally:
            return result

        pass

    def edit(self, map):
        result = 0

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            sql_str = "update eis_group set ID_ = '%s', COMPANY_ID_ = '%s', NAME_ = '%s', DESC_ = '%s', CREATE_DATE_ = '%s' WHERE (ID_ = '%s')" % (map["group_id"], map["company_id"], map["name"], map["desc"], dt, map["group_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result

        pass

    def delete(self, map):
        result = 0

        try:
            sql_str = "delete from eis_group WHERE ID_ = '%s'" % (map["group_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result
        pass

#部门管理
class DeptManageObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        self.user_table = Table(
            'eis_dept',
            self.metadata,
            Column('ID_', String),
            Column('COMPANY_ID_', String),
            Column('NAME_', String),
            Column('PARENT_ID_', String),
            Column('CREATE_DATE_', DATETIME),
            Column('DESC_', String)
        )

        self.metadata.create_all(self.engine)
        pass

    def create(self, map):
        result = ''

        # 生成ID
        tmp_did = str(uuid.uuid1()).replace('-', '')
        did = tmp_did.encode("UTF-8")

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            is_root = map["is_root"]

            if is_root == 1:
                sql_str = "insert into eis_dept(ID_, COMPANY_ID_, NAME_, DESC_, CREATE_DATE_) VALUE('%s', '%s', '%s', '%s', '%s')" % (did, map["company_id"], map["name"], map["desc"], dt)

            else:
                sql_str = "insert into eis_dept(ID_, COMPANY_ID_, NAME_, PARENT_ID_, DESC_, CREATE_DATE_) VALUE('%s', '%s', '%s', '%s', '%s', '%s')" % (did, map["company_id"], map["name"], map["parent_id"], map["desc"], dt)


            sql = text(sql_str)

            self.dbo.execute(sql)

            result = did

            pass
        except Exception, ex:
            print ex.message
            result = ''
        finally:
            return result


    def edit(self, map):
        result = 0

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            is_root = map["is_root"]

            if is_root == 1:
                sql_str = "update eis_dept set ID_ = '%s', COMPANY_ID_ = '%s', NAME_ = '%s', DESC_ = '%s', CREATE_DATE_ = '%s' WHERE ID_ = '%s'" % (map["dept_id"], map["company_id"], map["name"], map["desc"], dt, map["dept_id"])
            else:
                sql_str = "update eis_dept set ID_ = '%s', COMPANY_ID_ = '%s', NAME_ = '%s', PARENT_ID_ = '%s', DESC_ = '%s', CREATE_DATE_ = '%s' WHERE ID_ = '%s'" % (
                map["dept_id"], map["company_id"], map["name"], map["parent_id"], map["desc"], dt, map["dept_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result


    def delete(self, map):
        result = 0

        try:
            sql_str = "delete from eis_dept WHERE ID_ = '%s'" % (map["dept_id"])

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = 1
        except Exception, ex:
            print ex.message
            result = 0
        finally:
            return result


#菜单管理
class UrlManageObject:
    def __init__(self):
        connstr = eis["connectionstring"]

        self.engine = create_engine(connstr)

        self.dbo = self.engine.connect()

        self.metadata = MetaData()

        self.user_table = Table(
            'eis_url',
            self.metadata,
            Column('ID_', String),
            Column('COMPANY_ID_', String),
            Column('ICON_', String),
            Column('NAME_', String),
            Column('OREDR_', Integer),
            Column('URL_', String),
            Column('PARENT_ID_', String),
            Column('FOR_NAVIGATION_', Integer)
        )

        self.metadata.create_all(self.engine)
        pass

    def create(self, map):
        result = ''

        # 生成ID
        tmp_did = str(uuid.uuid1()).replace('-', '')
        did = tmp_did.encode("UTF-8")

        tmp_dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = tmp_dt.encode("UTF-8")

        try:
            is_root = map["is_root"]

            if is_root == 1:
                sql_str = "insert into eis_url(ID_, COMPANY_ID_, ICON_, NAME_, ORDER_, URL_, FOR_NAVIGATION_) VALUE('%s', '%s', '%s', '%s', '%s')" % (
                did, map["company_id"], map["name"], map["desc"], dt)

            else:
                sql_str = "insert into eis_url(ID_, COMPANY_ID_, ICON_, NAME_, ORDER_, URL_, PARENT_ID_, FOR_NAVIGATION_) VALUE('%s', '%s', '%s', '%s', '%s', '%s')" % (
                did, map["company_id"], map["name"], map["parent_id"], map["desc"], dt)

            sql = text(sql_str)

            self.dbo.execute(sql)

            result = did

            pass
        except Exception, ex:
            print ex.message
            result = ''
        finally:
            return result


        pass

    def edit(self, map):

        pass

    def delete(self, map):

        pass