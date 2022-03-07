from django.urls import path
from . import views

urlpatterns = [
    path('dates/', views.addDate, name='date')
]
