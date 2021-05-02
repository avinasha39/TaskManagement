from rest_framework import serializers 
from projectTask.models import Project
 
 
class ProjectSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Project
        fields = ('id',
                  'title',
                  'description',
                  'duration',
                  'photoFileName')