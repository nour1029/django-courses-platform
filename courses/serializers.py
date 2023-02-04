from rest_framwork import serializers
from .models import Course



class CourseSerializer(serializers.ModelSerialzer):
    class Meta:
        model = Course
        fields = '__all__'