from django.urls import path
from . import views

urlpatterns = [
    path('tournament/', views.tournament_view, name='tournament'),
    path('tournaments/add', views.addTournament, name='add-tournament'),
    path('tournaments/manage', views.manageTournaments, name='manage-tournament'),
    path('tournament/<int:tid>/', views.registerTournaments,
         name='register-tournament'),
    path('tournament/teamlist/<int:id>/',
         views.registeredTeamList, name='reg-team-list'),
    path('tournaments/<int:id>/',
         views.deleteTournament, name='delete-list'),
]
