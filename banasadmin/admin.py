from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

class DailyEntryDisplay(ImportExportModelAdmin):
    list_display=['name','cooler','date_added']
    list_display_links = ['name']

class CustomerDisplay(ImportExportModelAdmin):
    list_display=['name','phone_no']

class BillDisplay(ImportExportModelAdmin):
    list_display=['name','subtotal']

class paymentDisplay(ImportExportModelAdmin):
    list_display=['name','pay','date_payed']

# Register your models here.
admin.site.register(Bill,BillDisplay)
admin.site.register(Customer,CustomerDisplay)
admin.site.register(DailyEntry,DailyEntryDisplay)
admin.site.register(Payment,paymentDisplay)

