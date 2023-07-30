from django.contrib import admin

# Register your models here.
from .models import Company, Daraja, Profile


class DarajaAdmin(admin.ModelAdmin):
    list_display = ('turi', 'nomi')


admin.site.register(Daraja, DarajaAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'turi', 'publish', 'rating', 'inn')
    search_fields = ('name',)
    list_filter = ('name', 'publish',)



admin.site.register(Company, CompanyAdmin)