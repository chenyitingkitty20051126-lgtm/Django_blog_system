from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 如果是刚进入页面，显示一个空的注册表单
        form = UserCreationForm()
    else:
        # 处理填好的表单数据
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            # 保存新用户并获取用户对象
            new_user = form.save()
            # 注册成功后自动帮用户登录
            login(request, new_user)
            # 注册完跳转到首页
            return redirect('learning_logs:index')

    # 如果表单无效（如密码太短），会带回错误信息重新显示
    context = {'form': form}
    return render(request, 'registration/register.html', context)