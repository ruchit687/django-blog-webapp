from django.contrib import admin
from .models import Post

# Register your models here.
# to see post in admin we need to register
admin.site.register(Post)
