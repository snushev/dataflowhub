from rest_framework.routers import DefaultRouter
from .views import ETLJobViewset, ETLJobRunViewset


router = DefaultRouter()
router.register(r'jobs', ETLJobViewset, basename='etljob')
router.register(r'runs', ETLJobRunViewset, basename='etljobrun')

urlpatterns = router.urls
