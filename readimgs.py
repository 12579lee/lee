import pymysql
from dbutils.pooled_db import PooledDB
import numpy as np
import cv2
import pandas as pd
from PIL import Image
from io import BytesIO
import json

class Config(object):
    PYMYSQL_POOL = PooledDB(
        creator = pymysql,
        maxconnections=6,
        mincached=2,
        maxcached=5,
        maxshared=3,
        blocking=True,
        maxusage=None,
        setsession=[],
        ping=0,
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='database_1',
        charset='utf8'
    )

class SQLHelper(object):
    @staticmethod
    def open(cursor):
        POOL = Config.PYMYSQL_POOL
        conn = POOL.connection()
        cursor = conn.cursor(cursor=cursor)
        return conn,cursor

    @staticmethod
    def close(conn,cursor):
        conn.commit()
        cursor.close()
        conn.close()

    @classmethod
    def fetch_one(cls,sql,cursor=pymysql.cursors.DictCursor):
        conn,cursor = cls.open(cursor)
        cursor.execute(sql)
        obj = cursor.fetchone()
        cls.close(conn,cursor)
        return obj

    @classmethod
    def fetch_all(cls,sql,cursor=pymysql.cursors.DictCursor):
        conn, cursor = cls.open(cursor)
        cursor.execute(sql)
        obj = cursor.fetchall()
        cls.close(conn, cursor)
        return obj

conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       passwd = '123456',
                       charset = 'utf8')

obj = pd.DataFrame(SQLHelper.fetch_all("select filename from detect"),index=None)
for i in range(len(obj)):
    img = SQLHelper.fetch_one("select picture from detect where filename='"+obj.iat[i,0]+"'")

    str1 = np.asarray(SQLHelper.fetch_one("select picture from detect where filename='"+obj.iat[i,0]+"'"))

# print(str1)
# image = Image.fromarray(str1)  #将之前的矩阵转换为图片
# image.show()
# with open(r"D:\yolo-workimport torch\1.txt",'w',encoding='utf-8') as f:
#     f.write(str1)



# print(str1)
# bytes_stream = BytesIO(json.dumps(str1).encode())
# capture_img = Image.open(bytes_stream)
# capture_img = cv2.cvtColor(np.asarray(capture_img), cv2.COLOR_RGB2BGR)
# cv2.imshow("capture_img", capture_img)
# cv2.waitKey(0)

