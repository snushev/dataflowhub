from rest_framework import serializers
from .models import ETLJob, ETLJobRun


class ETLJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETLJob
        fields = '__all__'


class ETLJobRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ETLJobRun
        fields = '__all__'
