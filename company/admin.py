from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'industry', 'location', 'employee_count', 'rating')
    search_fields = ('name', 'industry', 'location')
