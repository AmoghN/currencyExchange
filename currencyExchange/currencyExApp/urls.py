from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^result$', views.result, name='result'),
    url(r'^hresult$', views.hresult, name='hresult')    
]
