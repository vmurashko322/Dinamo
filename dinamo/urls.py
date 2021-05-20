from django.urls import path
from dinamo.views import show_temp
urlpatterns = [
    path('', show_temp, name='show_temp'),
    ]