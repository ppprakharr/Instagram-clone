from post import views
from django.urls import path
app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
    path('new-post/',views.new_post,name='new-post'),
]