from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('add/',add, name='add'),
    path('completed/',completed, name='completed'),
    path('trash/',trash, name='trash'),
    path('about/',about, name='about'),

    path('hcomplete/<int:pk>',hcomplete,name = 'hcomplete'),
    path('hdelete/<int:pk>',hdelete,name = 'hdelete'),
    path('crestore/<int:pk>',crestore,name='crestore'),
    path('cdelete/<int:pk>',cdelete,name='cdelete'),
    path('trestore/<int:pk>',trestore,name='trestore'),
    path('tdelete/<int:pk>',tdelete,name='tdelete')
]