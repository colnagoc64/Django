from django.http import HttpResponse


def index(request):
    return HttpResponse("<body color=green>"+
                        "<hr>"+
                        "<h1>첫 페이지입니다.</h1>" +
                        "<hr>"+
                        "<a href=admin>to admin page</a><br>" +
                        "<a href=start>to start page</a><br>"+
                        "<a href=start2>to start2 page</a><br>" +
                        "<a href=start3>to start3 page</a><br>"+
                        "<a href=app1>to start5 page</a><br>" 
                        "</body>")