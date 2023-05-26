#
## 链接数据库
import time
import pymysql
from dbutils.pooled_db import PooledDB
from PIL import Image
import numpy as np
import pandas as pd
import readimgs
import cv2


# class Config(object):
#     PYMYSQL_POOL = PooledDB(
#         creator = pymysql,
#         maxconnections=6,
#         mincached=2,
#         maxcached=5,
#         maxshared=3,
#         blocking=True,
#         maxusage=None,
#         setsession=[],
#         ping=0,
#         host='localhost',
#         port=3306,
#         user='root',
#         password='123456',
#         database='database_1',
#         charset='utf8'
#     )
#
# class SQLHelper(object):
#     @staticmethod
#     def open(cursor):
#         POOL = Config.PYMYSQL_POOL
#         conn = POOL.connection()
#         cursor = conn.cursor(cursor=cursor)
#         return conn,cursor
#
#     @staticmethod
#     def close(conn,cursor):
#         conn.commit()
#         cursor.close()
#         conn.close()
#
#     @classmethod
#     def fetch_one(cls,sql,args,cursor=pymysql.cursors.DictCursor):
#         conn,cursor = cls.open(cursor)
#         cursor.execute(sql,args)
#         obj = cursor.fetchone()
#         cls.close(conn,cursor)
#         return obj
#
#     @classmethod
#     def fetch_all(cls,sql,args,cursor=pymysql.cursors.DictCursor):
#         conn, cursor = cls.open(cursor)
#         cursor.execute(sql, args)
#         obj = cursor.fetchall()
#         cls.close(conn, cursor)
#         return obj
#
#
# conn = pymysql.connect(host = 'localhost',
#                        port = 3306,
#                        user = 'root',
#                        passwd = '123456',
#                        charset = 'utf8')
# #
#
# def readData():
#     image_dir = r"D:\yolo-workimport torch\yolov5-master\runs\detect\exp2\000002.jpg"
    # x = Image.open(image_dir)  # 打开图片
    # data = np.asarray(x)  # 转换为矩阵
    # shape = data.shape  # 输出矩阵
    # np.set_printoptions(threshold=np.inf)
    # s1 = str(data).replace("[","").replace("]","").replace("\n ","")
    #
    # with open(r'D:\1.txt','w') as f:
    #     f.write(s1)



    # print(data)
    # nowTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # o = SQLHelper.fetch_one(
    #     "insert into detect(filename,picture,time) values(%s,%s,%s)",
    #     args=(dir, data, nowTime))


    # obj = pd.DataFrame(readimgs.SQLHelper.fetch_all("select filename from detect"), index=None)
    # for i in range(len(obj)):
    #     str1 = pd.DataFrame(readimgs.SQLHelper.fetch_one("select picture from detect where filename='" + obj.iat[i, 0] + "'"),index=None).replace("\n"," ")
    #     str2 = np.asarray(str1)
    #     print(str2)
    # s2 = np.loadtxt(r'D:\1.txt', dtype="int",encoding='utf-8')
    # #
    # s3 = s2.reshape(shape)
    # image = Image.fromarray(np.uint8(s3)) # 将之前的矩阵转换为图片
    # image.show()

# readData()
# image_dir = r"D:\yolo-workimport torch\yolov5-master\runs\detect\exp2\000002.jpg"
# with open(image_dir,'rb') as f:
#     image = f.read()
#     i = np.asarray(bytearray(image), dtype="uint8")
#     i = cv2.imdecode(i, cv2.IMREAD_COLOR)
# print(i)




# with open(r"D:\yolo-workimport torch\yolov5-master\runs\detect\exp2\000002.jpg",'rb') as f:
#     content = f.read()
#     with open(r"D://1.txt",'wb') as f:
#
#         f.write(content)

# with open(r"D://1.txt",'rb') as f:
#     con = f.read()
#
# print(con)
