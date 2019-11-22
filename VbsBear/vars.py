import pymysql

mysqldict = {'host':'localhost','user':'root','password':'123456','database':'vbsbeardb','charset':'utf8',}


conn = pymysql.connect(**mysqldict)
cursor = conn.cursor()
sql = 'insert into switch values(null, %s, %s, %s, %s)'
