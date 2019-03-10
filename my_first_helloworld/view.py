from django.shortcuts import render,redirect

'''这个view页面没有用'''
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'welcom.html', context)


def login_check(request):
    '''登录校验视图'''
    # 1.获取提交的用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember') # None on

    # 获取用户输入验证码
    vcode1 = request.POST.get('vcode')
    # 获取session中保存的验证码
    vcode2 = request.session.get('verifycode')

    # 进行验证码校验
    if vcode1 != vcode2:
        # 验证码错误
        return redirect('/login')

    # 2.进行登录的校验
    # 实际开发:根据用户名和密码查找数据库
    # 模拟: smart 123
    if username == 'smart' and password == '123':
        # 用户名密码正确，跳转到修改密码页面
        response = redirect('/change_pwd')

        # 判断是否需要记住用户名
        if remember == 'on':
            # 设置cookie username，过期时间1周
            response.set_cookie('username', username, max_age=7*24*3600)

        # 记住用户登录状态
        # 只有session中有islogin,就认为用户已登录
        request.session['islogin'] = True
        # 记住登录的用户名
        request.session['username'] = username
        # 返回应答
        return response
    else:
        # 用户名或密码错误，跳转到登录页面
        return redirect('/login')