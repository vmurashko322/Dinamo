from django.contrib import admin

# Register your models here.
from .models import OrderDetail, OrderItem
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['name','surname','email','adress','phone','pay_method','delivery_date']
    list_filter = ['order_date', 'pay_method']
    inlines = [OrderItemInline]

admin.site.register(OrderDetail, OrderDetailAdmin)
