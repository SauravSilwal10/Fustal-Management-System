from django.shortcuts import render, redirect
from teams.models import Team
from django.contrib.auth.decorators import login_required
# Create your views here.


# Create Team
@login_required(login_url="/login")
def createTeam(request):
    if request.method == 'POST':
        Name = request.POST['name-in']
        Address = request.POST['address-in']
        Phone_Number = request.POST['ph-number-in']
        Email = request.POST['email-in']
        Captain = request.POST['captain-in']
        Number = request.POST['no-of-players-in']
        Logo = request.POST['team-logo-in']
        create_team = Team(
            name=Name, address=Address, phone_number=Phone_Number, email=Email, captain_name=Captain, no_of_members=Number, logo=Logo, user=request.user)
        create_team.save()
        print("sucessfully saved")
        return redirect('/')
    return render(request, "teams.html")
