# from django.contrib import admin
# from app.models import AccessCount, Evaluation
# admin.site.register(AccessCount)
# admin.site.register(Evaluation)
from django.contrib import admin
from django.apps import apps

def get_admin_class(kls):
    class EveryThingAdmin(admin.ModelAdmin):
        list_display = [f.name for f in kls._meta.fields]
        list_editable = [f.name for f in kls._meta.fields
                        if f.name not in ('id', ) and f.editable == True]
    return EveryThingAdmin

models = apps.get_app_config('app').get_models()
for model in models:
    admin.site.register(model, get_admin_class(model))
