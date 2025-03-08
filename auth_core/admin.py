from django.contrib import admin

from auth_core.models import APIKey, APIKeyClient, ObjectPermission

admin.site.register(APIKey)
admin.site.register(ObjectPermission)
admin.site.register(APIKeyClient)
