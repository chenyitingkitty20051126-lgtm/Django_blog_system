from django.urls import path
from . import views  # 确保这里导入的是 views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    
    # 主题路由
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
    
    # 条目路由
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'),
    
    # 博客路由
    path('blogs/', views.blogs, name='blogs'),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),

    # 新增删除博文路由
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]