from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chara_index'),
    #path('store', views.store, name='_store'),
]