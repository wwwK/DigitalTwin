import pymysql

def createDatabase():
    # 打开数据库连接
    db = pymysql.connect(host="172.20.112.146",port=3306,user="newroot", passwd="newroot")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("CREATE DATABASE digitaltwin")

    db.close()


def createTable(db):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS WELDING")

    # 使用预处理语句创建表
    sql = """CREATE TABLE WELDING (
             A  FLOAT NOT NULL,
             V  FLOAT NOT NULL,
             L FLOAT NOT NULL )"""

    cursor.execute(sql)

def insertData(db,a,v,l):
    sql = "INSERT INTO WELDING (A, V, L) VALUES ('{0}','{1}', '{2}')".format(a, v, l)
    try:
        cursor=db.cursor()
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()

if __name__ =="__main__":
    # # 创建数据库
    # createDatabase()

    # 打开数据库连接
    db = pymysql.connect(host="172.20.112.146",port=3306,user="newroot", passwd="newroot", database="digitaltwin")
    createTable(db)
    insertData(db,0.0,0.0,0.0)
    # 关闭数据库连接
    db.close()
