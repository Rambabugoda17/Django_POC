from django.contrib import admin
from .models import Employee, Technologies


# Register your models here
class adminEmployee(admin.ModelAdmin):
    # the list only tells Django what to list on the admin site
    list_display = ["username", "email", "id"]
    search_fields = ('username', 'id')


admin.site.register(Employee, adminEmployee)
admin.site.register(Technologies)
