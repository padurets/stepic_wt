from django.http import HttpResponse, HttpResponseNotFound


def test(request, *args, **kwards):
    return HttpResponse('Ok')


def err(request, *args, **kwards):
    return HttpResponseNotFound('Ok')
