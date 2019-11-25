from django.contrib import admin
from .models import Company, Manager, Employee, Job, Workplace

admin.site.register(Company)
admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Job)
admin.site.register(Workplace)
