from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import ETLJob, ETLJobRun
from .serializers import ETLJobSerializer, ETLJobRunSerializer
from .tasks import run_etl_job

class ETLJobViewset(viewsets.ModelViewSet):
    queryset = ETLJob.objects.all()
    serializer_class = ETLJobSerializer

    @action(detail=True, methods=['post'])
    def run(self, request, pk=None):
        job = self.get_object()
        run_etl_job.delay(job.id)
        return Response({'message': f'ETL job {job.id} started!'}, status=status.HTTP_200_OK)

class ETLJobRunViewset(viewsets.ReadOnlyModelViewSet):
    queryset = ETLJobRun.objects.all()
    serializer_class = ETLJobRunSerializer

