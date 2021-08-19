# 建立 twii.db
import sqlite3

sql = 'create table if not exists twii(' \
      'id integer primary key autoincrement,' \
      'report_date integer,' \
      'stock_code varchar (10),' \
      'securities_name varchar (20),' \
      'yield_rate double,' \
      'div_year integer,' \
      'pe double,' \
      'pb double,' \
      'fin_report varchar (10),' \
      'memo varchar (50)' \
      ')'

conn = sqlite3.connect('twii.db')
cursor = conn.cursor()
cursor.execute(sql)

conn.commit()
conn.close()

print('twii 資料表建立成功')