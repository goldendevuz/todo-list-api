from rest_framework import routers
from .views import TodoViewSet

router = routers.SimpleRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls