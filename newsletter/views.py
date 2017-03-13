from django.shortcuts import render
from django.views import View
from .forms import ContactForm,BlogForm
from django.conf import settings
from django.core.mail import send_mail
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
		title='Contact Us'
		forms=ContactForm()
		if forms.is_valid():
			form_email=self.cleaned_data.get('email')
			form_full_name=self.cleaned_data.get('full_name')
			form_message=self.cleaned_data.get('message')
			subject="Site contact form"
			from_email=settings.EMAIL_HOST_USER
			to_email=[from_email]	
			contact_message= "%s:%s via %s"%(
		    		form_full_name,
		    		form_message,
		    		form_email)
			send_mail(subject, 
				contact_message,
				from_email,
				[to_email],
				fail_silently=True)
			

		context={
		"form":forms,
		"title":title
		}
		return render(request,"newsletter/form.html",context)


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
			# instance.title = "shivi"
			instance.save()
			

		context={
		'posts' : Post.objects.all()
		}
		return render(request,'newsletter/viewblog.html',context)


class WriteBlog(View):
	def get(self,request,*args,**kwargs):
		forms = BlogForm()
		context = {
		'forms' : forms,
		}
		return render(request,'newsletter/writeblog.html',context)