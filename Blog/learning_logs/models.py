from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """用户学习的主题。"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    # 核心修改：添加 owner 字段以关联用户 (练习 19-3)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text


class Entry(models.Model):
    """学到的有关某个主题的具体知识。"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回条目的字符串表示。"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text


class BlogPost(models.Model):
    """19-1: 博客文章模型。"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # 新增字段：允许为空，这样之前的博文不会报错
    attachment = models.FileField(upload_to='blog_attachments/', blank=True, null=True)
    # 19-5: 关联用户，实现权限控制
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回博文的标题。"""
        return self.title