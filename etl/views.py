from rest_framework import viewsets
from .models import ETLJob
from .serializers import ETLJobSerializer

class ETLJobViewset(viewsets.ModelViewSet):
    queryset = ETLJob.objects.all()
    serializer_class = ETLJobSerializer
