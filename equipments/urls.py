from django.urls import path
from . import views


urlpatterns = [
    path('equipments/add', views.createEquipment, name='add-equipments'),
    path('equipments/manage', views.manageEquipment, name='manage-equipments'),
    path('equipments/<int:id>',
         views.deleteEquipments, name='manage-equipments'),
]
