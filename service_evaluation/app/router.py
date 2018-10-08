from rest_framework import routers
from app.viewsets import AccessCountViewSet

router = routers.DefaultRouter()
router.register(r'count', AccessCountViewSet)