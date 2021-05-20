from django.conf.urls import url
from django.urls import path, re_path
from.views import movie_list,movie_detail
app_name='movies'
urlpatterns = [
    path('',movie_list,name='movie_list'),
    re_path(r'^(?P<genre_slug>[-\w]+)/$',movie_list,name='movie_list_by_genre'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',movie_detail,name='movie_detail')
]
