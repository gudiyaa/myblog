from django.conf.urls import url,include
from .views import Home,Contact,ViewBlog,WriteBlog,About
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
url(r'^$',Home.as_view(),name='home'),
url(r'^home/$',Home.as_view(),name='home'),
url(r'^about/$',About.as_view(),name='about'),
url(r'^contact/$',Contact.as_view(),name='contact'),
url(r'^blogs/$',ViewBlog.as_view(),name='blogs'),
url(r'^writeblog/$',WriteBlog.as_view(),name='writeblog'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)