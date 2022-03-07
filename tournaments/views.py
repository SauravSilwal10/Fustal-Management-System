from django.shortcuts import render, redirect
from tournaments.models import Tournament
from teams.models import Team
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# Add Tournament
@login_required(login_url="/login")
def addTournament(request):
    if request.method == 'POST':
        Name = request.POST['name-in']
        Description = request.POST['description-in']
        Prize = request.POST['prize-in']
        Banner = request.POST['banner-in']
        StartDate = request.POST['created-in']
        EndDate = request.POST['enddate-in']
        create_tournament = Tournament(name=Name, description=Description,
                                       prize=Prize, banner=Banner, created_at=StartDate, end_date=EndDate)
        create_tournament.save()
        messages.info(request, 'Tournament Created Successfully.')
        print("successfully saved")
    return render(request, "add_tournament.html")

# Tournament Page
def tournament_view(request):
    tournaments = Tournament.objects.all()
    context = {"tournament_list": tournaments}
    return render(request, "tournament.html", context)

# Manage Tournaments
@login_required(login_url="/login")
def manageTournaments(request):
    tournaments = Tournament.objects.all()
    context = {"tournament_list": tournaments}
    return render(request, "manage_tournaments.html", context)

# Register Teams into Tournament
@login_required(login_url="/login")
def registerTournaments(request, tid):
    if request.method == 'POST':
        tournament = Tournament.objects.get(id=tid)
        user = request.user
        teams = user.team
        print(teams)
        tournament.team.add(teams)
        tournament.save()
        return render(request, "home.html")
    else:
        tournament = Tournament.objects.get(id=tid)
        context = {"tournament": tournament}
        return render(request, "register_tournament.html", context)


# Registered Teams list in Tournament
@login_required(login_url="/login")
def registeredTeamList(request, id):
    tournament = Tournament.objects.get(id=id)
    teamlist = tournament.team.all()
    context = {"teamlist": teamlist}
    return render(request, "tournament_list.html", context)

# Delete Tournament
def deleteTournament(request, id):
    tournament = tournament = Tournament.objects.get(id=id)
    tournament.delete()
    messages.info(request, 'One tournament deleted successfully.')
    return render(request, "manage_tournaments.html")
