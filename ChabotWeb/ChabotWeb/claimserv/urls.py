from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
url(r'^addorder/', views.Claimadd, name='claimadd'),
url(r'^login/', auth_views.login, {'template_name': 'claimserv/login.html'}, name='login'),
url(r'^$', auth_views.login, {'template_name': 'claimserv/login.html'}, name='login'),
url(r'^logout/', views.Logout, name='logout'),
url(r'^chat/', views.Chat, name='chat'),
url(r'^Reply/', views.Reply, name='reply'),
]