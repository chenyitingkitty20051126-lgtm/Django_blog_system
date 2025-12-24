from django.contrib import admin
from .models import Topic, Entry, BlogPost

admin.site.register(Topic)
admin.site.register(Entry)

# 1. 定义一个管理类，决定列表页显示哪些列
class BlogPostAdmin(admin.ModelAdmin):
    # list_display 里的字段必须是你 BlogPost 模型中存在的
    list_display = ('title', 'date_added', 'owner')

# 2. 在注册模型时，把这个管理类也传进去
admin.site.register(BlogPost, BlogPostAdmin)