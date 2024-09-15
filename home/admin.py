from django.contrib import admin
from .models import Weblog,Video,Webhook,PompDump






admin.site.register(Weblog)

admin.site.register(Video)
admin.site.register(Webhook)
admin.site.register(PompDump)