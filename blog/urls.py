from django.conf.urls import url, include
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^about/$', views.about , name='about'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.show_article , name='article'),
    url(r'^search/$', views.search_product, name='search_product'),
    url(r'^search_r/$', views.search_r, name='search_r'),
    url(r'^new_article/$', views.new_article, name='new_article'),
    url(r'^auth/login/$',views.login_view, name='login_view' ),
    url(r'^auth/logout/$',views.logout_view, name='logout_view' )
]
