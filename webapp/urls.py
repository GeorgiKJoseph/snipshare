from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('home/',views.home,name='home'),                                                                  #home page
    path('x/<int:pk>/', views.code_detail, name='code_detail'),                                            #view code details
    path('add/new',views.add_new, name='add_new'),                                                         #add new pastebin
    path('search/',views.search, name='search'),                                                         #search

    path('',views.signup, name='signup'),                                                                  #redirect to signup page  
                                                                                                        
    url(r'^profile/edit/$',views.edit_profile, name='edit_profile'),                                       #edit profile
    url(r'^login/$', login, {'template_name': 'webapp/login.html'}),                                       #login
    url('logout/', logout, {'template_name': 'webapp/logout.html'}),                                       #logout
    url('signup/',views.signup,name='signup'),                                                             #signup
    url(r'^profile/view/$',views.view_profile, name='view_profile'),                                       #view self profile   
    url(r'^profile/view/(?P<pk>\d+)/$',views.view_profile, name='view_profile_with_pk'),                   #view others profile
    url(r'^profile/others/$',views.view_others, name='view_others'),                                     #view friends list
    url(r'^profile/friends/$',views.view_friends, name='view_friends'),                                     #view friends list
    url(r'^profile/friends/change/(?P<operation>.+)/(?P<pk>\d+)/$',views.change_friends,name='change_friends'),
    url(r'^profile/vote/(?P<pastebin_pk>\d+)/$',views.change_vote_status,name='change_vote_status'),    
]
