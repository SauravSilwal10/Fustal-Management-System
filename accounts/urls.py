from django.urls import path
from . import views


urlpatterns = [
    path('users/list', views.userList, name='users-list'),
    path('users/add', views.createUser, name='users-add'),
    path('users/list<int:id>/', views.updateUser, name='user'),
    path('users/list<int:id>/delete', views.deleteUser, name='delete'),
    path('update/<int:id>/', views.updateUser, name='users-update'),
]
