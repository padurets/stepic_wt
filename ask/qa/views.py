from django.http import HttpResponce


def test(request, *args, **kwards):
    return HttpResponce('Ok')
