#!/usr/bin/env python3
#
# Reporting tool that prints out reports based on the data in the DB newsdata

import psycopg2
import numpy as np

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
    GROUP BY authors.name,title ORDER BY views_num DESC;
    
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
    create view total_status as
    select date_trunc('day',time) as days,count(status) as t_status from log group by days;
    create view error_status as
    select date_trunc('day',time) as days, count(status) as e_status from log where status like '4%' group by days;

    select total_status.days,total_status.t_status, error_status.e_status
    from total_status join error_status
    on total_status.days = error_status.days and cast(error_status.e_status as float)/cast(total_status.t_status as float)*100 > 1
    group by total_status.days,total_status.t_status,error_status.e_status;
    ''' 
)

for count in range(0,len(queries)):
    c.execute(queries[count])
    # write report into .txt file
    report=c.fetchall()
    np.savetxt('report'+str(count)+'.txt',report,delimiter=' || ',fmt='%s')
db.close()
