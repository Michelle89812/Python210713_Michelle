# 請印出 employees 的所有欄位資料(含欄位名稱)
import sqlite3

conn = sqlite3.connect('emp.db')
cursor = conn.cursor()

cursor.execute('PRAGMA TABLE_INFO({})'.format('employees'))

names = [header[1] for header in cursor.fetchall()]

for name in names:
    print(name, end='\t')

print('\n_______________________________________________')

sql = 'SELECT emp_id, dept_id, emp_name, emp_salary, create_date FROM employees'
cursor.execute(sql)
emps = cursor.fetchall()

for emp in emps:
    print(('%-7d\t%-7d\t%-8s\t%10s\t%s\t' % (emp[0], emp[1], emp[2], ('$' + str(emp[3])), emp[4])))

