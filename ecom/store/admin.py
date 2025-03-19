from django.contrib import admin
from .models import Product,Customer,Order,Category
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
    
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
