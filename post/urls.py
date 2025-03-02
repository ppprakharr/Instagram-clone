from post import views
from django.urls import path
app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),
]