from django.contrib import admin
from post.models import Post, Tag, Follow, Stream
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Follow)
admin.site.register(Stream)

# Register your models here.
