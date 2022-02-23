from django.urls import path

from . import views

urlpatterns = [
    path('etudiants/', views.getEtudiants),
    path('get/etudiant/<int:id>/', views.getEtudiant),
    path('create/etudiant/', views.addEtudiant),
    path('update/etudiant/<int:id>/', views.updateEtudiant),
    path('delete/etudiant/<int:id>/', views.deleteEtudiant),
]