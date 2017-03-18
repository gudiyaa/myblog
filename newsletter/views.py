from django.shortcuts import render
from django.views import View
from .forms import BlogForm
from django.conf import settings
from .models import Post
# Create your views here.
class Home(View):
	def get(self,request,*args,**kwargs):
		return render(request,"newsletter/home.html",{})

	def post(self,request,*args,**kwargs):
		return render(request,"newsletter/home.html",{})


class About(View):
	def get(self,request,*args,**kwargs):
		return render(request,"newsletter/about.html",{})


class Contact(View):
	def get(self,request,*args,**kwargs):
		return render(request,"newsletter/form.html",{})


class ViewBlog(View):
	def get(self, request, *args, **kwargs):
		context={
		'posts' : Post.objects.all()
		}
		return render(request,'newsletter/viewblog.html',context)

	def post(self, request, *args, **kwargs):
		forms = BlogForm(request.POST or None)

		if forms.is_valid():
			instance = forms.save(commit = False)
			instance.author = request.user
			instance.save()
			
			poste = Post.objects.all()

		context={
		'posts' : poste
		}
		return render(request,'newsletter/viewblog.html',context)


class WriteBlog(View):
	def get(self,request,*args,**kwargs):
		forms = BlogForm()
		context = {
		'forms' : forms,
		}
		return render(request,'newsletter/writeblog.html',context)