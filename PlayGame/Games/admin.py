from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(AgeRestrictions)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Localization)
admin.site.register(Developer)
admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Status)
admin.site.register(Role)

@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('user',)

