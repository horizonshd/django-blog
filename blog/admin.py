from django.contrib import admin

from blog.models import Category,Tag,Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'category', 'author') # 显示的字段
    list_filter = ('category',)
    search_fields = ('title',)
    date_hierarchy = 'created_time'
    ordering = ('-modified_time',)
    fields = ('title','body', 'excerpt', 'category','tags','created_time', 'modified_time', 'author')  # 可修改值的字段

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostAdmin)
