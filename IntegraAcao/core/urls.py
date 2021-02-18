from django.urls import path
from .views import get_home
from .views import welcome
from .views import mylogout


urlpatterns = [
    path("page/", get_home),
    path('', welcome),
    path('logout/', mylogout, name='logout'),

]