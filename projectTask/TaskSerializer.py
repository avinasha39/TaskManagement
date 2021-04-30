from rest_framework import serializers 
from projectTask.models import Task
 
 
class TaskSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Task
        fields = ('id',
                  'title',
                  'description',
                  'startDate',
                  'endDate',
                  'project')