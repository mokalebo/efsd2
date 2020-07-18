from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    url(r'^accounts/login/$', LoginView.as_view(template_name='registration/login.html'), name="login"),
    url(r'^accounts/logout/$', LogoutView.as_view(), LogoutView.next_page, name="logout"),

   ]


## url(r'^login/$', views.LoginView.as_view(template_name=template_name), name='login'),
