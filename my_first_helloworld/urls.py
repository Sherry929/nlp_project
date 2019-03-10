"""my_first_helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import view
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^$', view.hello),
    #url(r'^login_check$', view.login_check), # 进行登录校验
    url(r'^', include('example.urls', namespace='example.urls')),

]





