from rest_framework import serializers
from .models import Species, Person

class SpeciesSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Species
        fields = '__all__'
        
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'