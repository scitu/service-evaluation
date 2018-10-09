
from random import choice, randint
from datetime import timedelta
from django.utils import timezone as tz
from django.db import transaction
from app.models import AccessCount

__PACKS = [
    {
        'url': 'http://analytics.service.sci.tu.ac.th/eval/',
        'path': '/eval/peoplefinder',
        'host': 'analytics.service.sci.tu.ac.th',
    },
    {
        'url': 'http://analytics.service.sci.tu.ac.th/eval/research',
        'path': '/eval/research',
        'host': 'analytics.service.sci.tu.ac.th',
    },
    {
        'url': 'http://peoplefinder.service.sci.tu.ac.th/',
        'path': '/',
        'host': 'peoplefinder.service.sci.tu.ac.th',
    },
]

protocol = 'http:'
ip = '127.0.0.1'
os = ['Window', 'Window', 'Window', 'Window', 'Linux', 'Android', 'Android', 'Mac OS', 'Mac OS', 'Mac OS']

AccessCount.objects.all().delete()
with transaction.atomic():
    for i in range(8416):
        pack = {
            **choice(__PACKS),
            'protocol': protocol,
            'ip': ip,
            'os': choice(os),
        }
        inst = AccessCount.objects.create(**pack)
        timeinst = tz.now() + timedelta(hours=randint(-(24*30*1), 0))
        while timeinst.hour > 17 and timeinst.hour < 8:
            timeinst = tz.now() + timedelta(hours=randint(-(24*30*1), 0))
        inst.timestamp = tz.now() + timedelta(hours=randint(-(24*30*1), 0))
        inst.save()
        print(timeinst)