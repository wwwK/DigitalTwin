import pymysql

def createDatabase():
    # 打开数据库连接
    db = pymysql.connect(host="172.20.120.7",port=3306,user="newroot", passwd="newroot")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("CREATE DATABASE digitaltwin")

    db.close()


def createTable(db):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # 使用预处理语句创建表
    sql = """CREATE TABLE EMPLOYEE (
             FIRST_NAME  CHAR(20) NOT NULL,
             LAST_NAME  CHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""

    cursor.execute(sql)


if __name__ =="__main__":
    # # 创建数据库
    # createDatabase()

    # 打开数据库连接
    db = pymysql.connect(host="172.20.120.7",port=3306,user="newroot", passwd="newroot", database="digitaltwin")
    createTable(db)
    # 关闭数据库连接
    db.close()
