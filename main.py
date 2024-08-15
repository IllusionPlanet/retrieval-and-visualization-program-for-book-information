import pymysql
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

db = pymysql.connect(host="localhost", user="root", passwd="root", db="mysqldb")
csr = db.cursor()
sql = "SELECT taleNumber FROM taleNumberByTime"
csr.execute(sql)
r = csr.fetchall()
Y = [r[0], r[1], r[2]]
sql2 = "SELECT time FROM taleNumberByTime"
csr.execute(sql2)
r = csr.fetchall()
X = [r[0], r[1], r[2]]
fig = plt.figure()
plt.bar(X, Y, 0.4, color="purple")
plt.xlabel("Days after 2020-07-28")
plt.ylabel("Tales Number")
plt.title("Bar Chart of Tales Number")

plt.show()
plt.savefig("barChartjpg")