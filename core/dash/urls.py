from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.dash, name='dash'),
    path('', views.home, name='home'),
    path('transfer', views.transfer, name='transfer'),
    path('history', views.historyview, name='history'),
    path('login', views.logger, name='logger'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('profile', views.userprofile, name='profile'),
    path('change_password', views.change_password, name='change_password'),
    path('id.me', views.idme_page, name='idme_page'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
    path('contact2', views.contact2, name='contact2'),
    path('aboutus', views.aboutus, name='aboutus'),
    
    

]
