from django.shortcuts import render

# Create your views here.

def start2(request):
    print('start2함수 호출됨')
    context ={"subject": "python", "class": "2100"}
    return render(request, "board/start2.html", context)

def start3(request):
    print('받은 데이터n1 : ',request.GET['n1'])
    print('받은 데이터n2 : ', request.GET['n2'])
    print('받은 데이터 subject : ', request.GET['subject'])
    print('start3함수 호출됨')
    n1= int(request.GET['n1'])
    n2= int(request.GET['n2'])
    plus = n1+n2
    subject= request.GET['subject']
    print(subject, '=================')
    context = {'plus':plus,"n1":n1,"n2":n2,"subject":subject}
    return render(request, "board/start3.html",context)

def start4(request):
    n1= int(request.POST['n1'])
    n2= int(request.POST['n2'])
    subject = request.POST['subject']
    print('start4함수 호출됨')
    plus = n1+n2
    context = {'plus': plus, "n1": n1, "n2": n2 ,"subject": subject}
    return render(request,"board/start4.html",context)
