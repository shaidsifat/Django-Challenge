from django.contrib import admin



from .models import company,Employee,OfficeResource

# Register your models here.


class  OfficeResourceAdmin(admin.ModelAdmin):
    

    list_display = ['name','reasontobuy','issuedate','returndate']
    list_field  = ['name','employee','office','reasontobuy','issuedate','returndate']


admin.site.register(company)
admin.site.register(Employee)
admin.site.register(OfficeResource,OfficeResourceAdmin)
