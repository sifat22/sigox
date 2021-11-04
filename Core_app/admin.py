from django.contrib import admin
from .models import Blog, Contact_Us
# Register your models here.


class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("blog_title",)}
    list_display = ('blog_title', 'created_date')


class contact_us_admin(admin.ModelAdmin):
    list_display = ('email', 'name', 'send_at')


admin.site.register(Blog, blogAdmin)
admin.site.register(Contact_Us, contact_us_admin)
