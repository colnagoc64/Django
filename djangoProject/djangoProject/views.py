from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def start(request): #views내에 정의된 함수는 반드시 파라메터를 하나 넣어주어야 한다.
    #클라이언트가 입력한 데이터를 받아주기 위한 변수임.!
    print('start함수가 호출되었음.!!!')
    return HttpResponse('<body bgcolor=red>' +
                        '<a href="http://www.naver.com">to naver</a><br>' +
                        '<a href="http://127.0.0.1:7777/start2">to start2</a><br>' +
                         '<a href="http://127.0.0.1:7777/start3">to start3</a><br>'
                        +'<a href="http://www.daum.net">to daum</a><br>' +
                        'i am a start page..@@@@</body>')

    #자동import: 해당 라이브러리위에서 실행해주면 됨.!

def start2(request):
    print('start2함수 호출됨.')
    return HttpResponse('<font color=red>start2페이지 호출되었음.</font>')

def start3(request):
    print('start3함수 호출됨.')
    return HttpResponse('<h1><a href="http://127.0.0.1:7777">to main</a><br>' +
                        '<a href="http://127.0.0.1:7777/start2">to start2</a></h1>')