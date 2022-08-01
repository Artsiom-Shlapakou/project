from django.contrib import admin

from employees.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'provider'
    )

    def change_view(self, request, object_id, extra_context=None):       
        self.exclude = ('last_login', )
        return super(EmployeeAdmin, self).change_view(request, object_id, extra_context)
