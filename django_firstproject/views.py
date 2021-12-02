from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello <a href='http://127.0.0.1:8000/index/'>back</a>")

def home(request):
    return HttpResponse("home")