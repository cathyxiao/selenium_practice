#encoding:utf-8
import MySQLdb,csv
#打开csv文件
file = '/Users/xiaoxiao/PycharmProjects/web/data/mysql.csv'
reader = csv.reader(file)
for line in reader:
    print line
connect = MySQLdb.connect(host=line[0],user=line[1],passwd=line[2],port=line[3],db=line[4])
