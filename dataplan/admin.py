from django.contrib import admin

from dataplan.models import Customer,Plan,Subscription


# Register your models here.
@admin.register(Plan)
class planAdmin(admin.ModelAdmin):
    list_display = ('name','price',)
    ordering = ('name',)
    search_fields = ('name','price',)
    list_filter = ('name', 'price',)
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('c_name','c_address','c_email',)
    ordering = ('c_name',)
    search_fields = ('c_name','c_address','c_email',)
    list_filter = ('c_name', 'c_address','c_email',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('plan','customer','a_date',)
    ordering = ('plan',)
    search_fields = ('plan','customer','a_date',)
    list_filter = ('plan', 'customer','a_date',)

