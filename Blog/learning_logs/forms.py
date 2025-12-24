from django import forms
from .models import Topic, Entry, BlogPost

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class BlogForm(forms.ModelForm):
    """用于发布博文的表单，包含附件上传字段"""
    class Meta:
        model = BlogPost
        # 必须确保包含 'attachment'，且名称与 models.py 一致
        fields = ['title', 'text', 'attachment'] 
        labels = {
            'title': '标题', 
            'text': '内容', 
            'attachment': '附件（图片/文档/代码）'
        }
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'placeholder': '在这里输入内容...'})
        }