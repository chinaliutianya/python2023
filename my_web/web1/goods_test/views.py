from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("测试")

def set_session(request):
    request.session['username']='lty'
    request.session['age']=47
    return HttpResponse('设置session')

def get_session(request):
    username=request.session['username']
    age=request.session['age']
    return HttpResponse('username:',username,'age:',age)

