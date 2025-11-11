from rest_framework import serializers
from .models import ETLJob

class ETLJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETLJob
        fields = '__all__'
