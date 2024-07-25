import pymysql

def linkMysql():
    db = pymysql.connect(host='10.6.3.123', user='root', password='LQDabc123@@@', database='blue')
    return db
# 提交数据到数据库，返回操作结果
def commitInfo(db,sql):
    cursor = db.cursor()
    # try:
    #     cursor.execute(sql)
    # except:
    #     print("出错了！！！")
    #     return "error"
    print("打印sql语句：",sql)
    cursor.execute(sql)
    print("事务更新成功！")
    db.commit()
    cursor.close()
    return cursor.fetchall()


