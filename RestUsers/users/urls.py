from django.urls import path
from .views import *

app_name = 'user'
urlpatterns = [
    path('user/create/', UserCreateView.as_view()),
    path('all/', UsersListView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
]