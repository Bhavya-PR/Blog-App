from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'index.html')

def detail(request,post_id):
    return HttpResponse(f"You are viewing the post detail page and the Id is {post_id}")

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url.")