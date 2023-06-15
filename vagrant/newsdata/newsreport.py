#!/usr/bin/env python3
#
# Reporting tool that prints out reports based on the data in the database

import psycopg2
import numpy as np

DBNAME = "news"

db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# queries list
queries = []
# query 1:
# General query to extract valuable information
# code examples to practice:
# select path, count(*) as num from log  group by path having path like '%candidate-is-jerk';
# select title,slug,count(*) as num from articles left join log on log.path like '%'||articles.slug group by title,slug order by num desc;
# delete views: DROP VIEW view_name;


# query 2:
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

# query 3:
# Who are the most popular article authors of all time?
queries.append(
    '''
    SELECT name, sum(views_num) as num
    FROM popular_articles_all_time
    GROUP BY name
    ORDER BY num DESC;
    '''
)

# query 4:
# On which days did more than 1% of requests lead to errors?
# show all 4xx errors and group time by day : 
# select date_trunc('day',time) as day, count(status) from log where status like '4%'group by day;
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
