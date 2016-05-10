# -*- coding: UTF-8 -*-
import MySQLdb
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="1234", db="dianping", charset="utf8")
cursor = conn.cursor()


k = open("sh.txt", "r")
shopid_list = k.readlines()
lens = len(shopid_list)
num = 0
for i in range(0,lens):
    sid = shopid_list[i][:-1]
    print sid,i,"  /  ",lens
    f = open("shmall/%s.txt"%sid,"r")
    content = f.readlines()
    lenc = len(content)    
    for j in range(1,lenc):
        review = content[j][:-1].split(",")
        if len(review) == 11:
            userid = review[0]
            user_nickname = review[1]
            user_contribution = review[2]
            rank_star = review[3]
            product = review[4]
            environment = review[5]
            service = review[6]
            cost_num = review[7]
            picture = review[8]
            comment_time = review[9]
            comment = str(review[10])
            values = (sid, userid, user_nickname, user_contribution, rank_star,\
                    product,environment,service,cost_num,picture,comment_time,comment)
            try:
                # print comment
                cursor.execute("insert into shoppingmall_sh values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", values)
                conn.commit()
            except Exception as E:
                pass
        # print comment

cursor.close()
conn.close()
