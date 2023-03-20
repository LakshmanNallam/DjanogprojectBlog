from django.contrib import admin

from .models import Post,Author,Tag

class PostAdmin(admin.ModelAdmin):
    list_filter=("author","title","data")
    prepopulated_fields={"slug":("title",)}
    list_display=("id","title","image","author")
    

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
