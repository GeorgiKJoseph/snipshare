from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('home/',views.home,name='home'),
    path('x/<int:pk>/', views.code_detail, name='code_detail'),
    path('add/new',views.add_new, name='add_new'),

    path('',views.signup, name='signup'),

    url(r'^profile/edit/$',views.edit_profile, name='edit_profile'),
    url(r'^login/$', login, {'template_name': 'webapp/login.html'}),
    url('logout/', logout, {'template_name': 'webapp/logout.html'}),
    url('signup/',views.signup,name='signup'),
    url(r'^profile/view/$',views.view_profile, name='view_profile'),


]
