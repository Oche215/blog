from django.contrib import admin
from  .models import Post

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display = ("text",)

admin.site.register(Post)
