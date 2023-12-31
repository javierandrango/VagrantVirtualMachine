#!/usr/bin/env python3
#
# Reporting tool that prints out reports based on the data in the DB newsdata

import psycopg2
import numpy as np
import pandas as pd
from datetime import date

DBNAME = "newsdata"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# queries list
queries = []

# query 1:
# What are the most popular three articles of all time?
queries.append(
    '''
    CREATE VIEW popular_articles_all_time AS
    SELECT authors.name, title, count(*) as views_num
    FROM articles
    LEFT JOIN log ON log.path like '%'||articles.slug
    LEFT JOIN authors ON articles.author = authors.id
    GROUP BY authors.name,title
    ORDER BY views_num DESC;
    SELECT title,views_num
    FROM popular_articles_all_time
    LIMIT 3;
    '''
)

# query 2:
# Who are the most popular article authors of all time?
queries.append(
    '''
    SELECT name, sum(views_num) as num
    FROM popular_articles_all_time
    GROUP BY name
    ORDER BY num DESC;
    '''
)

# query 3:
# On which days did more than 1% of requests lead to errors?
queries.append(
    '''
    CREATE view total_status AS
    SELECT date_trunc('day',time) AS days,COUNT(status) AS t_status
    FROM log
    GROUP BY days;
    CREATE VIEW error_status AS
    SELECT date_trunc('day',time) AS days, COUNT(status) AS e_status
    FROM log
    WHERE status LIKE '4%'
    GROUP BY days;
    SELECT total_status.days,total_status.t_status, error_status.e_status
    FROM total_status JOIN error_status
    ON total_status.days = error_status.days
    AND CAST(error_status.e_status AS FLOAT)/CAST(total_status.t_status AS FLOAT)*100 > 1
    GROUP BY total_status.days,total_status.t_status,error_status.e_status;
    '''
)

'''
# print individual report in txt file
for count in range(0, len(queries)):
    c.execute(queries[count])
    report = c.fetchall()
    np.savetxt('report' + str(count) + '.txt',
    report, delimiter=' || ', fmt='%s')
'''

reportList = []
for query in queries:
    c.execute(query)
    reportList.append(np.array(c.fetchall(), dtype='str'))

db.close()

pd.set_option('display.colheader_justify', 'left')
# What are the most popular three articles of all time?
dfReport1 = pd.DataFrame(reportList[0], columns=['Article name',
                                                 'Total Views'])

# Who are the most popular article authors of all time?
dfReport2 = pd.DataFrame(reportList[1], columns=['Author',
                                                 'Total Views'])

# On which days did more than 1% of requests lead to errors?
data = [[reportList[2][0][0][:11],
         str(float(reportList[2][0][2])/float(reportList[2][0][1])*100)]]
dfReport3 = pd.DataFrame(data, columns=['Year', 'Percentage'])

pageTitle = 'Report'

# Textual month, day and year
day = date.today()
datenow = day.strftime("%B %d, %Y")

report1Title = 'What are the most popular three articles of all time?'
report2Title = 'Who are the most popular article authors of all time?'
report3Title = 'On which days did more than 1% of requests lead to errors?'

html = '''
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Python DB-API report</title>
    <style media="screen">
      p{
        color: blue;
        text-align: center;
      }
      h1{
        color: green;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h1>%s</h1>
    <p>Report log analysis %s</p>
    <!--report to question 1-->
    <div>
        <h2>%s</h2>
        <p>%s</p>
    </div>
    <!--report to question 2-->
    <div>
        <h2>%s</h2>
        <p>%s</p>
    </div>
    <!--report to question 3-->
    <div>
        <h2>%s</h2>
        <p>%s</p>
    </div>

  </body>
</html>
''' % (pageTitle, datenow,
       report1Title, dfReport1.to_html(),
       report2Title, dfReport2.to_html(),
       report3Title, dfReport3.to_html())

with open('report_db_api.html', 'w') as f:
    f.write(html)
