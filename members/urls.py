from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.index, name='index'),
    path('members/indexpage',views.indexfunction, name='indexfunction')
]