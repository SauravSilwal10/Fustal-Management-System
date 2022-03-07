from django.shortcuts import render
from equipments.models import Equipment
import datetime
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create Equipment
@login_required(login_url="/login")
def createEquipment(request):
    if request.method == 'POST':
        Name = request.POST['eq-name']
        Brand = request.POST['eq-brand-in']
        Image = request.POST['eq-image-in']
        Price = request.POST['eq-price-in']
        create_equipment = Equipment(
            name=Name, brand=Brand, image=Image, created_at=date.today(), price=Price, user=request.user)
        create_equipment.save()
        messages.info(request, 'Equipment Added Successfully.')
        print("sucessfully saved")

    return render(request, "equipments.html")

# Manage Equipment
@login_required(login_url="/login")
def manageEquipment(request):
    Equipments = Equipment.objects.all()
    context = {'equipment_list': Equipments}
    return render(request, "manage_equipments.html", context)

# Delete Equipment
def deleteEquipments(request, id):
    equipments = equipments = Equipment.objects.get(id=id)
    equipments.delete()
    messages.info(request, 'One equipment deleted successfully.')
    return render(request, "equipments.html")
