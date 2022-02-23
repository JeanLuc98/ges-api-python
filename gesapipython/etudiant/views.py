from pickle import GET, TRUE
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EtudiantSerializer
from .models import Etudiant


#------------------------- Create your views here.--------------------------------------

#cette methode retourne tous les étudiants de la bd
@api_view(['GET'])
def getEtudiants(request):
    etudiants = Etudiant.objects.all()
    serialisation = EtudiantSerializer(etudiants, many=TRUE)
    return Response(serialisation.data)

#cette methode retourne un seul étudiant de la bd
@api_view(['GET'])
def getEtudiant(request, id):
    etudiant = Etudiant.objects.get(id = id)
    serialisation = EtudiantSerializer(etudiant)
    return Response(serialisation.data)

#cette methode permet de supprimer un étudiant de la bd
@api_view(['POST'])
def addEtudiant(request):
    serialisation = EtudiantSerializer(data = request.data, many=TRUE)
    if serialisation.is_valid():
        serialisation.save()
    return Response(serialisation.data)

#cette methode permet de modifier un étudiant de la bd
@api_view(['PUT'])
def updateEtudiant(request, id):
    etudiant = Etudiant.objects.get(id=id)
    serialisation = EtudiantSerializer(instance = etudiant, data = request.data)
    if serialisation.is_valid():
        serialisation.save()
    return Response(serialisation.data)

#cette methode permet de supprimer un étudiant de la bd
@api_view(['DELETE'])
def deleteEtudiant(request, id):
    etudiant = Etudiant.objects.get(id = id)
    etudiant.delete()
    return Response(f"L'étudiant {etudiant.prenom} {etudiant.nom} a bien été supprimé.")