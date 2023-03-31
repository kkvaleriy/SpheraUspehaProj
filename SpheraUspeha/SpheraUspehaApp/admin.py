from django.contrib import admin
from .models import Post, TlgrmUser

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(TlgrmUser, PostAdmin)
