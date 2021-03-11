from django.urls import path
from apps.posts.views import hello_world_view


app_name = 'posts'


urlpatterns = [
    path('', hello_world_view, name='hello_world')
]