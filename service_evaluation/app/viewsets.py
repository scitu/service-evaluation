from rest_framework import viewsets, mixins, permissions
from app.serializers import AccessCountSerializer
from app.models import AccessCount


class AccessCountViewSet(mixins.CreateModelMixin,
        viewsets.GenericViewSet):
    serializer_class = AccessCountSerializer
    queryset = AccessCount.objects.all()
    permission_classes = (permissions.AllowAny, )

    def get_serializer_context(self):
        return {'request': self.request}