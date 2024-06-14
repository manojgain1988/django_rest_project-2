from django.contrib import admin
from ProjectApp.models import Industry, Company, Person


# Register your models here.
class IndustryAdmin(admin.ModelAdmin):
    list_display=['id','name','code','created_at','updated_at']
admin.site.register(Industry,IndustryAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','name','industry','created_at','updated_at']
admin.site.register(Company,CompanyAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display=['id','name','created_at','updated_at']
admin.site.register(Person,PersonAdmin)