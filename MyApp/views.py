import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from MyApp.src.parsers.ParseConfig import MainStreamGet, SocialMediaGet
from MyApp.src.searcher.search import SearchNewsByKeyword


def index(request):
    return render_to_response('index.html')


def mainstream(request):
    return render_to_response('mainstream.html')


def socialmedia(request):
    return render_to_response('socialmedia.html')


def compare(request):
    return render_to_response('compare.html')


@csrf_exempt
def mainstreamprocess(request):
    if request.method == "POST":
        status = 'OK'
        if request.POST.get('durationtype') == '6':
            start = datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
            end = datetime.strptime(request.POST.get('end'), "%Y-%m-%d")

            if (end - start).days < 0:
                status = 'Fail'
        datas = MainStreamGet(request.POST.get('datasource'), request.POST.get('durationtype'),
                              request.POST.get('maxwords'), request.POST.get('start'), request.POST.get('end'))
        if len(datas) == 0:
            status = "Fail"

        if status != "Fail":
            request.session["maindatas"] = request.POST.get('datasource')
            request.session["maindurationtype"] = request.POST.get('durationtype')
            request.session["mainstart"] = request.POST.get('start')
            request.session["mainend"] = request.POST.get('end')
        return HttpResponse(json.dumps({
            "status": status,
            "length": len(datas),
            "result": datas
        }))


@csrf_exempt
def maincompareprocess(request):
    if request.method == "POST":
        status = 'OK'
        if request.POST.get('durationtype') == '6':
            start = datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
            end = datetime.strptime(request.POST.get('end'), "%Y-%m-%d")

            if (end - start).days < 0:
                status = 'Fail'
        datas = MainStreamGet(request.POST.get('datasource'), request.POST.get('durationtype'),
                              request.POST.get('maxwords'), request.POST.get('start'), request.POST.get('end'))
        if len(datas) == 0:
            status = "Fail"

        if status != "Fail":
            request.session["maindcompareatas"] = request.POST.get('datasource')
            request.session["maincomparedurationtype"] = request.POST.get('durationtype')
            request.session["maincomparestart"] = request.POST.get('start')
            request.session["maincompareend"] = request.POST.get('end')
        return HttpResponse(json.dumps({
            "status": status,
            "length": len(datas),
            "result": datas
        }))


@csrf_exempt
def socialmediacompareprocess(request):
    if request.method == "POST":
        # print request.POST.get('datasource')
        # # print request.POST.get('durationtype')
        # # print request.POST.get('maxwords')
        # print request.POST.get('start')
        # print request.POST.get('end')
        status = 'OK'
        if request.POST.get('durationtype') == '6':
            start = datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
            end = datetime.strptime(request.POST.get('end'), "%Y-%m-%d")
            if (end - start).days < 0:
                status = 'Fail'

        data = SocialMediaGet(request.POST.get('datasource'), request.POST.get('durationtype'),
                              request.POST.get('maxwords'), request.POST.get('start'), request.POST.get('end'))
        if len(data) == 0:
            status = "Fail"

        if status != "Fail":
            request.session["socialcomparedatas"] = request.POST.get('datasource')
            request.session["socialcomparedurationtype"] = request.POST.get('durationtype')
            request.session["socialcomparestart"] = request.POST.get('start')
            request.session["socialcompareend"] = request.POST.get('end')

        return HttpResponse(json.dumps({
            "status": status,
            "length": len(data),
            "result": data
        }))


@csrf_exempt
def mainsocialcompareprocess(request):
    if request.method == "POST":
        # print request.POST.get('datasource')
        # # print request.POST.get('durationtype')
        # # print request.POST.get('maxwords')
        # print request.POST.get('start')
        # print request.POST.get('end')
        status = 'OK'
        if request.POST.get('durationtype') == '6':
            start = datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
            end = datetime.strptime(request.POST.get('end'), "%Y-%m-%d")
            if (end - start).days < 0:
                status = 'Fail'

        data2 = SocialMediaGet(request.POST.get('datasource1'), request.POST.get('durationtype'),
                               request.POST.get('maxwords'), request.POST.get('start'), request.POST.get('end'))
        data1 = MainStreamGet(request.POST.get('datasource2'), request.POST.get('durationtype'),
                              request.POST.get('maxwords'), request.POST.get('start'), request.POST.get('end'))

        if len(data1) == 0:
            status = "Fail"
        if len(data2) == 0:
            status = "Fail"

        if status != "Fail":
            request.session["socialcomparedatas"] = request.POST.get('datasource')
            request.session["socialcomparedurationtype"] = request.POST.get('durationtype')
            request.session["socialcomparestart"] = request.POST.get('start')
            request.session["socialcompareend"] = request.POST.get('end')
            request.session["maindcompareatas"] = request.POST.get('datasource')
            request.session["maincomparedurationtype"] = request.POST.get('durationtype')
            request.session["maincomparestart"] = request.POST.get('start')
            request.session["maincompareend"] = request.POST.get('end')

        return HttpResponse(json.dumps({
            "status": status,
            "length": len(data1) + len(data2),
            "result1": data1,
            "result2": data2
        }))


@csrf_exempt
def socialmediaprocess(request):
    if request.method == "POST":
        # print request.POST.get('datasource')
        # # print request.POST.get('durationtype')
        # # print request.POST.get('maxwords')
        # print request.POST.get('start')
        # print request.POST.get('end')
        status = 'OK'
        if request.POST.get('durationtype') == '6':
            start = datetime.strptime(request.POST.get('start'), "%Y-%m-%d")
            end = datetime.strptime(request.POST.get('end'), "%Y-%m-%d")
            if (end - start).days < 0:
                status = 'Fail'

        data = SocialMediaGet(request.POST.get('datasource'), request.POST.get('durationtype'),
                              request.POST.get('maxwords'), request.POST.get('start'), request.POST.get('end'))
        if len(data) == 0:
            status = "Fail"

        if status != "Fail":
            request.session["socialdatas"] = request.POST.get('datasource')
            request.session["socialdurationtype"] = request.POST.get('durationtype')
            request.session["socialstart"] = request.POST.get('start')
            request.session["socialend"] = request.POST.get('end')

        return HttpResponse(json.dumps({
            "status": status,
            "length": len(data),
            "result": data
        }))


def mainstreamdetail(request):
    source = request.session.get("maindatas", default=None)
    duration = request.session.get("maindurationtype", default=None)
    start = request.session.get("mainstart", default=None)
    end = request.session.get("mainend", default=None)
    # print source
    # print duration
    # print start
    # print end

    keyword = request.GET.get('keyword')
    if str(source) == "":
        print "a"
        source = "news=0"
        duration = "2"
    processedsplit = keyword.split(" ")
    likestr = ''
    for w in processedsplit:
        likestr += '%' + str(w).upper()
    likestr += '%'
    # source = source.split(',')

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


def socialmediadetail(request):
    source = request.session.get("socialdatas", default=None)
    duration = request.session.get("socialdurationtype", default=None)
    start = request.session.get("socialstart", default=None)
    end = request.session.get("socialend", default=None)
    # print source
    # print duration
    # print start
    # print end

    keyword = request.GET.get('keyword')
    if str(source) == "":
        print "a"
        source = "news=0"
        duration = "2"
    processedsplit = keyword.split(" ")
    likestr = ''
    for w in processedsplit:
        likestr += '%' + str(w).upper()
    likestr += '%'
    # source = source.split(',')

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
            'select title,link,postdate from socialmedia.allsingaporestuff where keyword like \'' + likestr + '\' and postdate>' + sqlend)
    if '1' in source:
        sqllist.append(
            'select title,link,postdate from socialmedia.mothership where keyword like \'' + likestr + '\' and postdate>' + sqlend)
    if '2' in source:
        sqllist.append(
            'select title,link,postdate from socialmedia.mustsharenews where keyword like \'' + likestr + '\' and postdate>' + sqlend)
    newslist = SearchNewsByKeyword(sqllist)
    return render_to_response('topicdetail.html', {'newslist': newslist})
