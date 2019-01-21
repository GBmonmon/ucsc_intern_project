import mysql.connector
import os
import shutil


try:
    cnx = mysql.connector.connect(user='root', password='gbmonmon',
                                  host='172.17.0.2',database='test')
except:
    cnx = mysql.connector.connect(user='root', password='gbmonmon',
                                  host='172.17.0.3',database='test')

cursor = cnx.cursor()
cursor.execute('use test;')

query = ('select * from test;')
cursor.execute(query)

myquery = list()
for row in cursor:
    print(row)
    myquery.append(row)

html = '''<head> data in mysql </head>

<body>
{}
</body>
'''.format(myquery)

with open('index.html', 'w') as fh:
    fh.write(html)

path = '/usr/local/tomcat/webapps'
os.mkdir(path + '/myapp')
shutil.move("./index.html", path + '/myapp/' + 'index.html')



cnx.close()
cursor.close()
