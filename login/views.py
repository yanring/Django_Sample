# coding=utf-8
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User


# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


class UserFormRegist(forms.Form):
    username = forms.EmailField(label='注册邮箱', max_length=100, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'E-mail', 'style': 'width:20%'}))
    password = forms.CharField(label='密码', widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'placeholder': "password", 'style': 'width:20%'}))
    password_check = forms.CharField(label='确认密码', widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'placeholder': "check again", 'style': 'width:20%'}))


def regist(req):
    if req.method == 'POST':
        uf = UserFormRegist(req.POST)
        login_flag = False
        # print(type(req))
        # print(req)
        if uf.is_valid():
            # 获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password_check = uf.cleaned_data['password_check']
            test = 'test'
            print(password)
            print(password_check == password)
            # 添加到数据库
            if password == password_check:

                try:
                    print(User.objects.create(username=username, password=password))
                    print("check")
                    success = True
                    print(test)
                    test = 'test2'
                    return render_to_response('regist.html', {'uf': uf, 'success': success, 'test': test},
                                              context_instance=RequestContext(req))
                except Exception as e:
                    login_flag = False
                    error = True
                    print(e)
                    test = 'test'
                    error_info = e
                    return render_to_response('regist.html',
                                              {'uf': uf, 'error': error, 'error_info': error_info, 'test': test},
                                              context_instance=RequestContext(req))

            else:
                error = True
                print(test)
                error_info = "Please input the same password twice"
                print(error_info)
                return render_to_response('regist.html', {'uf': uf, 'error': error, 'error_info': error_info},
                                          context_instance=RequestContext(req))


        else:
            return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))
    uf = UserFormRegist()
    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))


def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        # print()
        if uf.is_valid():
            username = uf.cleaned_data['username']
            # print(uf.cleaned_data)
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact=username, password__exact=password)
            if user:
                respoense = HttpResponseRedirect('/home')
                respoense.set_cookie('username', username, 3600)
                return respoense
            else:
                error = True
                return render_to_response('login.html', {'uf': uf, 'error': error},
                                          context_instance=RequestContext(req))
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))
