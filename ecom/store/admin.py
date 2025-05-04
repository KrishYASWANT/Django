from django.contrib import admin
from .models import Product,Customer,Order,Category,Profile
from django.contrib.auth.models import User
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
admin.site.register(Profile)


# Mix profile info and user info
class ProfileInline(admin.StackedInline):
	model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

# Unregister the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)