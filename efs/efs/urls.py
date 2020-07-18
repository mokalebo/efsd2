from django.contrib import admin
from django.conf.urls import  include,url
from django.urls import path
from django.contrib.auth import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    url(r'^accounts/login/$', views.LoginView.as_view, name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view, name='logout', kwargs={'next_page': '/'}),
]

## url(r'^login/$', views.LoginView.as_view(template_name=template_name), name='login'),
