import re
from MyApp.src.searcher.search import SearchKeywordsByConfig


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


def MainStreamGet(source, duration, maxwords, start, end):
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


def SocialMediaGet(source, duration, maxwords, start, end):
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
