"""mail_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import threading
from django.contrib import admin
from django.urls import path
# from .views import home
# from .views import send_gmail
from .views import HomeView


handler404 = HomeView.as_view()
handler500 = HomeView.as_view()
handler503 = HomeView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home, name="home"),
    path('', HomeView.as_view(), name='send_mail'),
    # path('send_mail/', send_gmail, name="send_mail"),
]


