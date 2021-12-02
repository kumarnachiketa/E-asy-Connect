from django.shortcuts import render

def blog(request):
    return render(request, 'blog.html')
def blogdetail(request):
    return render(request, 'blog-detail.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def projectdetail(request):
    return render(request, 'project-detail.html')

# Create your views here.
