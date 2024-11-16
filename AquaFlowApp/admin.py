from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Login_model)
admin.site.register(authority_model)
admin.site.register(staff_model)
admin.site.register(user_model)
admin.site.register(time_model)
admin.site.register(area_model)
admin.site.register(assignedwork_model)
admin.site.register(report_model)
admin.site.register(reading_model)
admin.site.register(application_model)
admin.site.register(complaints_model)
admin.site.register(bill_model)

