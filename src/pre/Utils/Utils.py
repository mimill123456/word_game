import pymysql
import MySQLdb
import MySQLdb.cursors  #使用字典返回数据内容需要额外引用该模块


class Util:

    def write_to_file(self,filename, con):
        file_object = open(filename, 'w', encoding='utf-8')
        file_object.write(con)
        file_object.close()


    def select_mysql(self,sql):
        db = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='ff14',
                             cursorclass=MySQLdb.cursors.DictCursor, charset='utf8mb4')
        cursor = db.cursor()
        cursor.execute(sql)
        rs = cursor.fetchall()
        # rs = rs.encode('utf-8').decode('unicode_escape')
        # print(type(rs))
        # print(rs)
        cursor.close()
        db.close()
        return rs


    def commit_to_mysql(self,sql):
        # try:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='game',
                                   charset='utf8mb4')
            cur = conn.cursor()
            res = ()
            if isinstance(sql,list):
                for s in sql:
                    print(s)
                    cur.execute(s)
            if isinstance(sql,str):
                print(sql)
                cur.execute(sql)
                res = cur.fetchall()
            conn.commit()
            cur.close()
            conn.close()
            return res
    # except Exception:
    #     print('数据库出错')

