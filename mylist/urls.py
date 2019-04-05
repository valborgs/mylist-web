from django.urls import path
from .views import mainpage, mylist, title_detail, production_list, prodution_detail, genre_list, genre_detail, year_list, year_detail

app_name = 'mylist'

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('mylist/', mylist, name='mylist'),
    path('mylist/<title_slug>', title_detail, name='title_detail'),
    path('mylist/production_list/', production_list, name='production_list'),
    path('mylist/production_list/<production_slug>', prodution_detail, name='production_detail'),
    path('mylist/genre_list/', genre_list, name='genre_list'),
    path('mylist/genre_list/<genre_slug>', genre_detail, name='genre_detail'),
    path('mylist/year_list/', year_list, name='year_list'),
    path('mylist/year_list/<year_slug>', year_detail, name='year_detail'),
]
