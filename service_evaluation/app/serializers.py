from rest_framework import serializers
from app.models import AccessCount

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AccessCountSerializer(serializers.ModelSerializer):

    def create(self, validated_data, *args, **kwargs):
        try:     
            ip = get_client_ip(self.context['request'])
            validated_data['ip'] = ip
        except Exception:
            pass
        return super(AccessCountSerializer, self).create(validated_data, *args, **kwargs)

    class Meta:
        model = AccessCount
        exclude = ('ip', )