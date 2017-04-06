import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from MyApp.src.parsers.ParseConfig import MainStreamGet, SocialMediaGet, SearchMainKeyword, SearchSocialKeyword
from MyApp.src.searcher.search import SearchNewsByKeyword


def index(request):
    return render_to_response('index.html')


def mainstream(request):
    return render_to_response('mainstream.html')


def socialmedia(request):
    return render_to_response('socialmedia.html')


def compare(request):
    return render_to_response('compare.html')


def contactus(request):
    return render_to_response('contact.html')


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
            request.session["socialcomparedatas"] = request.POST.get('datasource2')
            request.session["comparedurationtype"] = request.POST.get('durationtype')
            request.session["comparestart"] = request.POST.get('start')
            request.session["compareend"] = request.POST.get('end')
            request.session["maindcompareatas"] = request.POST.get('datasource2')
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

    newslist = SearchMainKeyword(source, duration, start, end, keyword)
    return render_to_response('topicdetail.html', {'newslist': newslist})


def comparemainstreamdetail(request):
    source = request.session.get("maindcompareatas", default=None)
    duration = request.session.get("comparedurationtype", default=None)
    start = request.session.get("comparestart", default=None)
    end = request.session.get("compareend", default=None)
    keyword = request.GET.get('keyword')

    newslist = SearchMainKeyword(source, duration, start, end, keyword)
    return render_to_response('topicdetail.html', {'newslist': newslist})


def socialmediadetail(request):
    source = request.session.get("socialdatas", default=None)
    duration = request.session.get("socialdurationtype", default=None)
    start = request.session.get("socialstart", default=None)
    end = request.session.get("socialend", default=None)
    keyword = request.GET.get('keyword')

    newslist = SearchSocialKeyword(source, duration, start, end, keyword)
    return render_to_response('topicdetail.html', {'newslist': newslist})


def comparesocialmediadetail(request):
    source = request.session.get("socialcomparedatas", default=None)
    duration = request.session.get("comparedurationtype", default=None)
    start = request.session.get("comparestart", default=None)
    end = request.session.get("compareend", default=None)
    keyword = request.GET.get('keyword')
    newslist = SearchSocialKeyword(source, duration, start, end, keyword)
    return render_to_response('topicdetail.html', {'newslist': newslist})
