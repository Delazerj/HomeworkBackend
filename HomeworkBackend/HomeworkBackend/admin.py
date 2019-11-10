from django.contrib import admin

from . import models


class CountryAdmin(admin.ModelAdmin):
    list_display = (['name'])


class SnowboarderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'country')
    search_fields = (['first_name', 'last_name'])
    sortable_by = (['last_name'])


admin.site.register(models.Country, CountryAdmin)

admin.site.register(models.Snowboarder, SnowboarderAdmin)

