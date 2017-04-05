import json

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import os

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from MyApp.src.mainstream.KeywordGen import GetKeywordByCustom, GetKeywordByDuration
from MyApp.src.draw.wordscloud import DrawStraitsTimesCloud
from MyApp.src.parsers.KeywordParser import ParseKeywords
from MyApp.src.searcher.search import searchByKeyword, SearchNewsByKeyword


def index(request):
    return render_to_response('index.html')


@csrf_exempt
def homeprocess(request):
    if request.method == "POST":
        ParseKeywords(2016, 11)
        keywords = DrawStraitsTimesCloud(2016, 11, 100)
        status = 'OK'
        if len(keywords) == 0:
            status = "Fail"
        return HttpResponse(json.dumps({
            "status": status,
            "length": len(keywords),
            "result": keywords
        }))


@csrf_exempt
def mainstreamprocess(request):
    if request.method == "POST":
        # print request.POST.get('datasource')
        # # print request.POST.get('durationtype')
        # # print request.POST.get('maxwords')
        # print request.POST.get('start')
        # print request.POST.get('end')
        data = []
        status = 'OK'
        if request.POST.get('durationtype') == '6':
            start = datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
            end = datetime.strptime(request.POST.get('end'), "%Y-%m-%d")

            if (end - start).days < 0:
                status = 'Fail'
            else:
                data = GetKeywordByCustom(request.POST.get('datasource'), request.POST.get('maxwords'),
                                          request.POST.get('start'), request.POST.get('end'))
        else:
            data = GetKeywordByDuration(request.POST.get('datasource'), request.POST.get('durationtype'),
                                        request.POST.get('maxwords'))

        if len(data) == 0:
            status = "Fail"
        return HttpResponse(json.dumps({
            "status": status,
            "length": len(data),
            "result": data
        }))


def homedetail(request):
    newslist = searchByKeyword(2016, 11, request.GET.get("keyword"))
    return render_to_response('topicdetail.html', {'newslist': newslist})


def detail(request):
    source = request.GET.get('datasource')
    duration = request.GET.get('duration')

    start = request.GET.get('start')
    end = request.GET.get('end')
    keyword = request.GET.get('keyword')
    if str(source) == "":
        print "a"
        source = "0,"
        duration = "2"
    processedsplit = keyword.split(" ")
    likestr = ''
    for w in processedsplit:
        likestr += '%' + str(w).upper()
    likestr += '%'
    source = source.split(',')

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
            'select title,link,postdate from newsdata.straitstimesnewdata where keyword like \'' + likestr + '\' and postdate>' + sqlend)
    if '1' in source:
        sqllist.append(
            'select title,link,postdate from newsdata.todayonlinenewdata where keyword like \'' + likestr + '\' and postdate>' + sqlend)
    if '2' in source:
        sqllist.append(
            'select title,link,postdate from newsdata.channelaisadata where keyword like \'' + likestr + '\' and postdate>' + sqlend)
    newslist = SearchNewsByKeyword(sqllist)
    return render_to_response('topicdetail.html', {'newslist': newslist})


def mainstream(request):
    return render_to_response('mainstream.html')
