# import pymysql
#
#
# conf = {
#     'host':'127.0.0.1',
#     'user':'root',
#     'password':'123456',
#     'port':3307,
#     'db':'pcik_log_dep',
#     'max_allowed_packet':10,
#     'read_timeout':100,
#
# }
#
# conn = pymysql.Connect(**conf)
# cur = conn.cursor()
# sql ='select accidx,count(*),date(logintime) as login,date(logouttime) as logout from t_user_logout group by accidx,login,logout;'
# # cur.execute('select *from t_user_logout limit 1002')
# cur.execute(sql)
#
# data = cur.fetchall()
#
# for i in data:
#     print (i)
#
#
# cur.close()
# # conn.close()



import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(os.path.dirname(os.path.abspath(__file__)))

print (os.path.join(BASE_DIR,'ddd'))