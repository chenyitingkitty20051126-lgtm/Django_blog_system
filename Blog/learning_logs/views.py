from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry, BlogPost
from .forms import TopicForm, EntryForm, BlogForm

# --- 权限辅助函数 ---

def _check_topic_owner(topic, request):
    """私有辅助函数：确认当前用户是主题的所有者，否则抛出 404"""
    if topic.owner != request.user:
        raise Http404

# --- 核心页面 ---

def index(request):
    """学习笔记首页。"""
    return render(request, 'learning_logs/index.html')

def blogs(request):
    """显示所有博客文章（按时间顺序）。"""
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'learning_logs/blogs.html', context)

# --- 主题管理 ---

@login_required
def topics(request):
    """显示主题。超级用户看全部，普通用户看自己的。"""
    if request.user.is_superuser:
        topics = Topic.objects.order_by('date_added')
    else:
        topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有条目。"""
    topic = get_object_or_404(Topic, id=topic_id)
    _check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    return render(request, 'learning_logs/new_topic.html', {'form': form})

@login_required
def delete_topic(request, topic_id):
    """删除主题"""
    topic = get_object_or_404(Topic, id=topic_id)
    _check_topic_owner(topic, request)
    if request.method == 'POST':
        topic.delete()
        return redirect('learning_logs:topics')
    return render(request, 'learning_logs/delete_topic_confirm.html', {'topic': topic})

# --- 博客管理 ---

@login_required
def new_post(request):
    """发布新博客，支持文件上传"""
    if request.method != 'POST':
        form = BlogForm()
    else:
        # 核心：必须包含 files=request.FILES
        form = BlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('learning_logs:blogs')
    return render(request, 'learning_logs/new_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    """编辑现有的博文，支持更换附件"""
    post = get_object_or_404(BlogPost, id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = BlogForm(instance=post)
    else:
        # 使用统一的 BlogForm 并传入 files 参数
        form = BlogForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:blogs')
    return render(request, 'learning_logs/edit_post.html', {'post': post, 'form': form})

@login_required
def delete_post(request, post_id):
    """删除博客文章"""
    post = get_object_or_404(BlogPost, id=post_id)
    if post.owner == request.user or request.user.is_superuser:
        if request.method == 'POST':
            post.delete()
            return redirect('learning_logs:blogs')
        return render(request, 'learning_logs/delete_post_confirm.html', {'post': post})
    raise Http404

# --- 条目管理 ---

@login_required
def new_entry(request, topic_id):
    """在特定主题中添加新条目。"""
    topic = get_object_or_404(Topic, id=topic_id)
    _check_topic_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic  # 关联到当前主题
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
            
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    _check_topic_owner(topic, request)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    return render(request, 'learning_logs/edit_entry.html', {'entry': entry, 'topic': topic, 'form': form})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic
    _check_topic_owner(topic, request)
    if request.method == 'POST':
        entry.delete()
        return redirect('learning_logs:topic', topic_id=topic.id)
    return render(request, 'learning_logs/delete_entry_confirm.html', {'entry': entry, 'topic': topic})