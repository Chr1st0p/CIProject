import re
from MyApp.src.searcher.search import SearchKeywordsByConfig, SearchNewsByKeyword
from datetime import datetime


def MainStreamByCustom(source, maxwords, start, end):
    lis = re.findall(r'[0-9]', str(source))
    sqllist = []

    if '0' in lis:
        sqllist.append(
            'select keyword from newsdata.straitstimesnewdata where postdate> \'' + start + '\' and postdate< \'' + end + '\'')
    if '1' in lis:
        sqllist.append(
            'select keyword from newsdata.todayonlinenewdata where postdate> \'' + start + '\' and postdate< \'' + end + '\'')
    if '2' in lis:
        sqllist.append(
            'select keyword from newsdata.channelaisadata where postdate> \'' + start + '\' and postdate< \'' + end + '\'')

    return SearchKeywordsByConfig(sqllist, maxwords)


def MainStreamByDuration(source, duration, maxwords):
    if duration == '0':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 WEEK)'
    elif duration == '1':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 WEEK)'
    elif duration == '2':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    elif duration == '3':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 MONTH)'
    elif duration == '4':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 3 MONTH)'
    elif duration == '5':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 6 MONTH)'
    else:
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'

    lis = re.findall(r'[0-9]', str(source))
    sqllist = []

    if '0' in lis:
        sqllist.append('select keyword from newsdata.straitstimesnewdata where postdate>' + sqlend)
    if '1' in lis:
        sqllist.append('select keyword from newsdata.todayonlinenewdata where postdate>' + sqlend)
    if '2' in lis:
        sqllist.append('select keyword from newsdata.channelaisadata where postdate>' + sqlend)

    return SearchKeywordsByConfig(sqllist, maxwords)


def GetMainStreamNews(source, duration, maxwords, start, end):
    lis = re.findall(r'[0-9]', str(source))
    sqllist = []
    if duration == '6':
        sqlend = '\'' + start + '\' and postdate< \'' + end + '\''
    elif duration == '0':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 WEEK)'
    elif duration == '1':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 WEEK)'
    elif duration == '2':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    elif duration == '3':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 MONTH)'
    elif duration == '4':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 3 MONTH)'
    elif duration == '5':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 6 MONTH)'
    else:
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'

    if '0' in lis:
        sqllist.append('select keyword from newsdata.straitstimesnewdata where postdate>' + sqlend)
    if '1' in lis:
        sqllist.append('select keyword from newsdata.todayonlinenewdata where postdate>' + sqlend)
    if '2' in lis:
        sqllist.append('select keyword from newsdata.channelaisadata where postdate>' + sqlend)

    return SearchKeywordsByConfig(sqllist, maxwords)


def GetSocialMediaNews(source, duration, maxwords, start, end):
    sqllist = []
    lis = re.findall(r'[0-9]', str(source))
    if duration == '6':
        sqlend = '\'' + start + '\' and postdate< \'' + end + '\''
    elif duration == '0':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 WEEK)'
    elif duration == '1':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 WEEK)'
    elif duration == '2':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    elif duration == '3':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 MONTH)'
    elif duration == '4':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 3 MONTH)'
    elif duration == '5':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 6 MONTH)'
    else:
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'

    if '0' in lis:
        sqllist.append('select keyword from socialmedia.allsingaporestuff where postdate>' + sqlend)
    if '1' in lis:
        sqllist.append('select keyword from socialmedia.mothership where postdate>' + sqlend)
    if '2' in lis:
        sqllist.append('select keyword from socialmedia.mustsharenews where postdate>' + sqlend)

    return SearchKeywordsByConfig(sqllist, maxwords)


def SearchMainByKeyword(source, duration, start, end, keyword):
    if str(source) == "":
        print "a"
        source = "news=0"
        duration = "2"
    processedsplit = keyword.split(" ")
    likestr = ''
    for w in processedsplit:
        likestr += '%' + str(w).upper()
    likestr += '%'
    if duration == '6':
        sqlend = ' \'' + start + '\' and postdate< \'' + end + '\';'
    elif duration == '0':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 WEEK)'
    elif duration == '1':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 WEEK)'
    elif duration == '2':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    elif duration == '3':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 MONTH)'
    elif duration == '4':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 3 MONTH)'
    elif duration == '5':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 6 MONTH)'
    else:
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    sqllist = []

    if '0' in source:
        sqllist.append(
            'select title,link,postdate from newsdata.straitstimesnewdata where UPPER(keyword) like \'' + likestr + '\' and postdate>' + sqlend)
    if '1' in source:
        sqllist.append(
            'select title,link,postdate from newsdata.todayonlinenewdata where UPPER(keyword) like \'' + likestr + '\' and postdate>' + sqlend)
    if '2' in source:
        sqllist.append(
            'select title,link,postdate from newsdata.channelaisadata where UPPER(keyword) like \'' + likestr + '\' and postdate>' + sqlend)

    return SearchNewsByKeyword(sqllist)


def SearchSocialByKeyword(source, duration, start, end, keyword):
    if str(source) == "":
        source = "news=0"
        duration = "2"
    processedsplit = keyword.split(" ")
    likestr = ''
    for w in processedsplit:
        likestr += '%' + str(w).upper()
    likestr += '%'
    if duration == '6':
        sqlend = ' \'' + start + '\' and postdate< \'' + end + '\';'
    elif duration == '0':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 WEEK)'
    elif duration == '1':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 WEEK)'
    elif duration == '2':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    elif duration == '3':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 2 MONTH)'
    elif duration == '4':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 3 MONTH)'
    elif duration == '5':
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 6 MONTH)'
    else:
        sqlend = ' DATE_SUB(CURDATE(), INTERVAL 1 MONTH)'
    sqllist = []

    if '0' in source:
        sqllist.append(
            'select title,link,postdate from socialmedia.allsingaporestuff where UPPER(keyword) like \'' + likestr + '\' and postdate>' + sqlend)
    if '1' in source:
        sqllist.append(
            'select title,link,postdate from socialmedia.mothership where UPPER(keyword) like \'' + likestr + '\' and postdate>' + sqlend)
    if '2' in source:
        sqllist.append(
            'select title,link,postdate from socialmedia.mustsharenews where UPPER(keyword) like \'' + likestr + '\' and postdate>' + sqlend)

    return SearchNewsByKeyword(sqllist)


# Avoid SQL injection
def IsValidDate(datestring):
    try:
        datetime.strptime(datestring, "%Y-%m-%d")
        return True
    except:
        return False
