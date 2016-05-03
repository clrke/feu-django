from django.contrib import admin

from django.contrib import admin
from django.apps import apps

class RecordedModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_at', 'updated_at')


app = apps.get_app_config('tasks')

for model_name, model in app.models.items():
    admin.site.register(model, RecordedModelAdmin)

