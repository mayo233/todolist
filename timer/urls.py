from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='timer_index'),
    path('store', views.store, name='timer_store'),
]