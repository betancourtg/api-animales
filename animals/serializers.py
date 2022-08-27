from rest_framework import serializers
from animals.models import Animals
from animals import models

class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = '__all__'