from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^item/(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^drafts/$', views.item_draft_list, name='item_draft_list'),
    url(r'^item/(?P<pk>\d+)/publish/$', views.item_publish, name='item_publish'),
    url(r'^item/(?P<pk>\d+)/remove/$', views.item_remove, name='item_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/likes/$', views.add_likes_to_post, name='add_likes_to_post'),
    url(r'^post/(?P<pk>\d+)/unlike/$', views.unlike_post, name='unlike_post'),   
]
