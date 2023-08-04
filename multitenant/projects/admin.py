from django.contrib import admin
from .models import Emp


class EmployeeAdmin(admin.ModelAdmin):
    # the list only tells Django what to list on the admin site
    list_display = ["name", "emp_id", "department"]
    search_fields = ('name', 'department')


# Register your models here.
# admin.site.register(Emp)
admin.site.register(Emp, EmployeeAdmin)
