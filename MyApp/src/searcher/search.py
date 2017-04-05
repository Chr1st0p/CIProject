import mysql.connector
from mysql.connector import Error
from MyApp.src.utils.Config import BackColors, DbConfig
import re
from MyApp.src.utils.Paths import Paths
from wordcloud import WordCloud


def SearchKeywordsByConfig(sqllist, maxwords):
    cachedstopwords = open(Paths.textPath + 'stopwords.txt').read()
    stopwords = cachedstopwords.split('\n')
    global cursor, cnn
    keyword = []
    for sql in sqllist:
        try:
            cnn = mysql.connector.connect(**DbConfig.newsDataConfig)
            cursor = cnn.cursor(buffered=True)
            cursor.execute(sql)
            keyword.append(cursor.fetchall())
        except Error as e:
            print BackColors.WARNING + "error" + BackColors.ENDC
            print e
        finally:
            cursor.close()
            cnn.close()
    tokens = re.findall(r"[\w']+", "".join(''.join(elem) for elem in keyword[0]))

    lowerToken = [word.lower() for word in tokens]

    filteredToken = [word for word in lowerToken if word not in stopwords]
    w = WordCloud().process_text(' '.join(filteredToken))
    w = sorted(w.items(), reverse=True, key=lambda x: x[1])
    if maxwords == '0':
        mx = 10
    elif maxwords == '1':
        mx = 20
    elif maxwords == '2':
        mx = 50
    elif maxwords == '3':
        mx = 100
    elif maxwords == '4':
        mx = 200
    elif maxwords == '5':
        mx = 500
    else:
        mx = 200
    return w[:mx]


def SearchNewsByKeyword(sqlist):
    news = []
    for sql in sqlist:
        try:
            cnn = mysql.connector.connect(**DbConfig.newsDataConfig)
            cursor = cnn.cursor(buffered=True)
            cursor.execute(sql)
            row = cursor.fetchone()
            while row is not None:
                if 'newsdata.straitstimesnewdata' in sql:
                    news.append({'title': row[0], 'link': row[1], 'postdate': row[2], 'source': 'StraitsTimes'})
                    row = cursor.fetchone()
                elif 'newsdata.todayonlinenewdata' in sql:
                    news.append({'title': row[0], 'link': row[1], 'postdate': row[2], 'source': 'TodayOnline'})
                    row = cursor.fetchone()
                elif 'newsdata.channelaisadata' in sql:
                    news.append({'title': row[0], 'link': row[1], 'postdate': row[2], 'source': 'ChannelAsia'})
                    row = cursor.fetchone()
                elif 'socialmedia.allsingaporestuff' in sql:
                    news.append({'title': row[0], 'link': row[1], 'postdate': row[2], 'source': 'All Singapore Stuff'})
                    row = cursor.fetchone()
                elif 'socialmedia.mothership' in sql:
                    news.append({'title': row[0], 'link': row[1], 'postdate': row[2], 'source': 'MotherShip'})
                    row = cursor.fetchone()
                elif 'socialmedia.mustsharenews' in sql:
                    news.append({'title': row[0], 'link': row[1], 'postdate': row[2], 'source': 'MustShareNews'})
                    row = cursor.fetchone()
        except Error as e:
            print sql
            print BackColors.WARNING + "error" + BackColors.ENDC
            print e
        finally:
            cursor.close()
            cnn.close()

    return news
