from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('x/<int:pk>/', views.code_detail, name='code_detail'),
    path('add/new',views.add_new, name='add_new'),
    path('signup',views.signup, name='signup'),
]
