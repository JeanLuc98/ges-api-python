from dataclasses import fields
from rest_framework import serializers

from etudiant.models import Etudiant

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'