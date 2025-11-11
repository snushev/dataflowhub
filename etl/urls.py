from rest_framework.routers import DefaultRouter
from .views import ETLJobViewset

router = DefaultRouter()
router.register(r'etl-jobs', ETLJobViewset, basename='etljob')

urlpatterns = router.urls
