from django.contrib import admin
from .models import Email,Blacklist


class EmailAdminPageSEttings(admin.ModelAdmin):
    list_display = ('sender','email_text','created_at')
    search_fields = ('sender',)

admin.site.register(Email,EmailAdminPageSEttings)

class BlacklistAdminPageSettings(admin.ModelAdmin):
    list_display = ('sender','added_at')
    search_fields = ('sender',)

admin.site.register(Blacklist,BlacklistAdminPageSettings)